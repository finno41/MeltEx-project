var popupWindow = document.getElementById("popup-window");
var failHTML = "<div class='alert alert-danger' role='alert'>Your listings were not uploaded due to an error, please check the sheet</div>"
var bannerContainer = document.getElementById("banner-placement");

function getSuccessHTML(numberUploaded) {
  return `<div class='alert alert-success' role='alert'>${numberUploaded} listings were uploaded successfully</div>`
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
