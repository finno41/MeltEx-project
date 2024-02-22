var popupLinks = document.querySelectorAll(".popup-link");
var closeButtons = document.querySelectorAll(".close-button");
var popupWindow = document.querySelector(".popup-window");
var popUpContent = document.getElementById("view-listing-content")


function showRegisterInterestForm(registerInterestButton) {
  var registerInterestForm = document.getElementById("register-interest-form");
  registerInterestForm.style.display = "block";
  registerInterestButton.style.display = "none";
  popupWindow.scrollTop = popupWindow.scrollHeight;
}

function hideRegisterInterestForm() {
  var registerInterestForm = document.getElementById("register-interest-form");
  var registerInterestButton = document.getElementById("register-interest-button")
  registerInterestForm.style.display = "none";
  registerInterestButton.style.display = "block";
}

function addEventListenerToRegisterInterest() {
  var registerInterestButton = document.getElementById("register-interest-button")
  registerInterestButton.addEventListener("click", () => { showRegisterInterestForm(registerInterestButton) })
}

function addEventListenerToCancelButton() {
  var cancelButton = document.getElementById("cancel-register-interest-button")
  cancelButton.addEventListener("click", hideRegisterInterestForm)
}
function closePopUpWindow() {
  popupWindow.style.display = "none";
  popUpContent.innerHTML = "";
}

closeButtons.forEach(function (closeButton) {
  closeButton.addEventListener("click", function () {
    closePopUpWindow()
  });
});


document.addEventListener('click', function (event) {
  showListingPopUp = document.getElementById("show-listing-pop-up")
  if (event.target !== showListingPopUp && !showListingPopUp.contains(event.target)) {
    closePopUpWindow()
  }
});

addPopUpEventListener()

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
          popUpContent.innerHTML = html;
          popupWindow.style.display = "block"
          addEventListenerToRegisterInterest()
          addEventListenerToCancelButton()
        })
        .catch(error => {
          console.error('Error fetching HTML:', error);
        });
    })
  })
}
