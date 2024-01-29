var popupLink = document.getElementById("popup-link");
var popupWindow = document.getElementById("popup-window");
var closeButtons = document.querySelectorAll(".close-button");
console.log(closeButtons)

popupLink.addEventListener("click", function (event) {
  event.preventDefault();
  popupWindow.style.display = "block";
});

closeButtons.forEach(function (closeButton) {
  console.log(closeButton)
  closeButton.addEventListener("click", function () {
    popupWindow.style.display = "none";
  });
});
