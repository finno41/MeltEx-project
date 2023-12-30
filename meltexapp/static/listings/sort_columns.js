var counter = 0;
var prev_column = null;
var baseUrl = window.location.origin + "/";
var params = new URLSearchParams(window.location.search);

document.addEventListener('DOMContentLoaded', function () {
  var sortableColumns = document.querySelectorAll('.sortable_column');
  addColumnsEventListener(sortableColumns)
})



function addColumnsEventListener(sortableColumns) {


  sortableColumns.forEach(function (column) {
    var columnId = column.id;


    function buildQueryString() {
      if (prev_column === columnId) {
        counter++;
      }
      else {
        counter = 0
      }
      console.log(params)
      prev_column = columnId
      var queryString = Object.keys(params)
        .map(key => {
          if (Array.isArray(params[key])) {
            return params[key].map(value => encodeURIComponent(key) + '=' + encodeURIComponent(value));
          } else {
            return encodeURIComponent(key) + '=' + encodeURIComponent(params[key]);
          }
        })
        .flat()
        .join('&');

      if (counter % 3 !== 2) {
        queryString += "&" + encodeURIComponent("sort") + "=" + encodeURIComponent(columnId);
      }

      if (counter % 3 === 0) {
        queryString += "&" + encodeURIComponent("ascending") + "=" + encodeURIComponent("true");
      }

      return queryString;
    }

    function addEventListeners() {
      column.addEventListener('click', function () {
        var listingsTable = document.getElementById('listings-table');
        var queryString = buildQueryString();
        var url = baseUrl + "listings/load_listings_table?" + queryString;
        fetch(url)
          .then(response => response.text())
          .then(data => {
            listingsTable.innerHTML = data;
            var sortableColumns = document.querySelectorAll('.sortable_column');
            addColumnsEventListener(sortableColumns)
          });
      });
    }
    addEventListeners();
  });
};