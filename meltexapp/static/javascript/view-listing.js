var popupLinks = document.querySelectorAll(".popup-link");
var closeButtons = document.querySelectorAll(".close-button");
var popupWindow = document.querySelector(".popup-window");
var popUpContent = document.getElementById("view-listing-content")
const csrftoken = getCookie('csrftoken');

function addFetchToInterestSubmit(listingId) {
  document.getElementById("confirm-register-interest-button").addEventListener("click", function () {
    var form = document.getElementById("expression-interest-form");
    url = `/listing/${listingId}/register_interest`
    formData = new FormData(form)
    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken
      },
      body: formData
    })
      .then(response => {
        return response.json().then(jsonResponse => ({ response, jsonResponse }));
      })
      .then(({ response, jsonResponse }) => {
        if (response.status === 200) {
          displayBannerNotification("success", jsonResponse.message, "top-of-listing-info", "listing-info-column");
          hideRegisterInterestForm();
        } else {
          displayBannerNotification("fail", jsonResponse.error, "top-of-listing-info", "listing-info-column");
          hideRegisterInterestForm();
        }
      })
      .catch(error => {
        // Get error message from response and show in error banner
      });
  })
}

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
          addFetchToInterestSubmit(listingId)
        })
        .catch(error => {
          console.error('Error fetching HTML:', error);
        });
    })
  })
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
