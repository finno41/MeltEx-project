var popupLinks = document.querySelectorAll(".popup-link");
var closeButtons = document.querySelectorAll(".close-button");
var popupWindow = document.getElementById("popup-window");
var popUpContent = document.getElementById("view-listing-content")

popupLinks.forEach(function (popupLink) {
  popupLink.addEventListener("click", function (event) {
    event.preventDefault();
    popupWindow.style.display = "block";
  });
})

closeButtons.forEach(function (closeButton) {
  closeButton.addEventListener("click", function () {
    popupWindow.style.display = "none";
    popUpContent.innerHTML = "";
  });
});

popupLinks.forEach(popupLink => {
  console.log(popupLink)
  const listingId = popupLink.id;
  popupLink.addEventListener("click", function (event) {
    event.preventDefault();
    const url = `/listings/show_listing/${listingId}`;
    fetch(url)
      .then(response => response.text())
      .then(html => {
        popUpContent.innerHTML = html
      })
      .catch(error => {
        console.error('Error fetching HTML:', error);
      });
  })
})
