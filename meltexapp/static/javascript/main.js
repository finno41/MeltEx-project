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

if (typeof closeButtons !== 'undefined') {
  closeButtons.forEach(function (closeButton) {
    closeButton.addEventListener("click", function () {
      popupWindow.style.display = "none";
    });
  });
}

function checkTickboxes(tickboxIds) {
  console.log(tickboxIds)
  tickboxIds.forEach(function (tickboxId) {
    var tickbox = document.getElementById(tickboxId)
    tickbox.checked = true
  })
}

function addHoverstate(hoverButtonId, hoverContentId) {
  const hoverButton = document.getElementById(hoverButtonId)
  const hoverContent = document.getElementById(hoverContentId)
  hoverButton.addEventListener("mouseover", function () {
    hoverContent.style.display = "block"
  })
  hoverButton.addEventListener("mouseout", function () {
    hoverContent.style.display = "none"
  })
}
