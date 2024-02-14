var popupWindow = document.querySelector(".popup-window");
var closeButtons = document.querySelectorAll(".close-button");
var popupLinks = document.querySelectorAll(".popup-link");

console.log(document.querySelectorAll(".popup-window"))
popupLinks.forEach(function (popupLink) {
  popupLink.addEventListener("click", function (event) {
    event.preventDefault();
    popupWindow.style.display = "block";
  });
})



closeButtons.forEach(function (closeButton) {
  closeButton.addEventListener("click", function () {
    popupWindow.style.display = "none";
  });
});
