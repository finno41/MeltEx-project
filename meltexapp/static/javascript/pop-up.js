var popupLink = document.getElementById("popup-link");
var popupWindow = document.getElementById("popup-window");
var closeButtons = document.querySelectorAll(".close-button");

popupLink.addEventListener("click", function (event) {
  event.preventDefault();
  popupWindow.style.display = "block";
});

closeButtons.forEach(function (closeButton) {
  closeButton.addEventListener("click", function () {
    popupWindow.style.display = "none";
  });
});
