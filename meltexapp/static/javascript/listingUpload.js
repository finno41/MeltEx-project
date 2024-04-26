var popupWindow = document.getElementById("upload-popup-window");
var bannerContainer = document.getElementById("banner-placement");

function getSuccessHTML(numberUploaded) {
  return `<div class='alert alert-success' role='alert'>${numberUploaded} listings were uploaded successfully</div>`
}

function getFailHTML(message) {
  return `<div class='alert alert-danger' role='alert'>${message}</div>`
}

$(document).ready(function () {
  $("#listings-upload-form").submit(function (e) {
    e.preventDefault();
    $("#listings-upload-submit").attr("hidden", true);
    $("#upload-loading-spinner").removeAttr('hidden');

    var formData = new FormData(this);

    $.ajax({
      type: "POST",
      url: "/listings/import/excel",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        popupWindow.style.display = "none";
        $("#upload-loading-spinner").attr("hidden", true);
        $("#listings-upload-submit").removeAttr('hidden');
        if (response.success) {
          data = JSON.parse(response.data);
          let successHTML = getSuccessHTML(data.length)
          bannerContainer.innerHTML = successHTML;
        } else {
          data = response
          let failHTML = getFailHTML(data["message"])
          bannerContainer.innerHTML = failHTML;
        }
      },
      error: function (xhr, status, error) {
        popupWindow.style.display = "none";
        $("#upload-loading-spinner").attr("hidden", true);
        $("#listings-upload-submit").removeAttr('hidden');
        bannerContainer.innerHTML = failHTML;
      }
    });
  });
});
