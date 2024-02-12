var popupWindow = document.getElementById("popup-window");
var closeButtons = document.querySelectorAll(".close-button");
var popupLinks = document.querySelectorAll(".popup-link");


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
