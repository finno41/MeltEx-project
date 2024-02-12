$(document).ready(function () {
  $(".info-button").submit(function (e) {
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
