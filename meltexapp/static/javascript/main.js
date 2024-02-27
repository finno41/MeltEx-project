function displayBannerNotification(type, message, topOfPageId, parentScrollElementId) {
  var topOfPageElement = document.getElementById(topOfPageId)
  var parentScrollElement = document.getElementById(parentScrollElementId)
  const alertTypes = {
    "success": "alert-success",
    "fail": "alert-danger"
  }
  var alertType = alertTypes[type]
  html = `<div class='alert ${alertType}' role='alert'>${message}</div>`
  topOfPageElement.innerHTML = html
  parentScrollElement.scrollTop = 0;
}

function submitForm(formId) {
  document.getElementById(formId).submit();
}
