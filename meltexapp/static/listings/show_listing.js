function showRegisterInterestForm() {
  var registerInterestForm = document.getElementById("register-interest-form");
  registerInterestForm.style.display = "block";
}

function hideRegisterInterestForm() {
  var registerInterestForm = document.getElementById("register-interest-form");
  registerInterestForm.style.display = "none";
}

function addEventListenerToRegisterInterest() {
  registerInterestButton.addEventListener("click", showRegisterInterestForm)
}
