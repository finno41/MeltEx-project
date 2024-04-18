var popupWindow = document.querySelector(".popup-window");
var closeButtons = document.querySelectorAll(".close-button");
var popupLinks = document.querySelectorAll(".popup-link");

popupLinks.forEach(function (popupLink) {
  popupLink.addEventListener("click", function (event) {
    event.preventDefault();
    var popupWindow = document.querySelector(".popup-window");
    popupWindow.style.display = "block";
  });
})



closeButtons.forEach(function (closeButton) {
  closeButton.addEventListener("click", function () {
    var popupWindow = document.querySelector(".popup-window");
    popupWindow.style.display = "none";
  });
});
