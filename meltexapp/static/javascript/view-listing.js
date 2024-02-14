var popupLinks = document.querySelectorAll(".popup-link");
var closeButtons = document.querySelectorAll(".close-button");
var popupWindow = document.querySelector(".popup-window");
var popUpContent = document.getElementById("view-listing-content")


closeButtons.forEach(function (closeButton) {
  closeButton.addEventListener("click", function () {
    popupWindow.style.display = "none";
    popUpContent.innerHTML = "";
  });
});
// displayPopUpEventListener()
addPopUpEventListener()

// function displayPopUpEventListener() {
//   var popupLinks = document.querySelectorAll(".popup-link");
//   popupLinks.forEach(function (popupLink) {
//     popupLink.addEventListener("click", function (event) {
//       event.preventDefault();
//       popupWindow.style.display = "block";
//     });
//   })
// }
function addPopUpEventListener() {
  var popupLinks = document.querySelectorAll(".popup-link");
  popupLinks.forEach(popupLink => {
    const listingId = popupLink.id;
    popupLink.addEventListener("click", function (event) {
      event.preventDefault();
      const url = `/listings/show_listing/${listingId}`;
      fetch(url)
        .then(response => response.text())
        .then(html => {
          popUpContent.innerHTML = html
        })
        .then(popupWindow.style.display = "block")
        .catch(error => {
          console.error('Error fetching HTML:', error);
        });
    })
  })
}
