var popupLinks = document.querySelectorAll(".popup-link");
var closeButtons = document.querySelectorAll(".close-button");
var listingInfoColumn = document.querySelector(".listing-info-column");
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
  listingInfoColumn.scrollTop = listingInfoColumn.scrollHeight;
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
