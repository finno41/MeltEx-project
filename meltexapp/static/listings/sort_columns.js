var counter = 0;
var prev_column = null;
var baseUrl = window.location.origin + "/";
console.log(baseUrl)

document.addEventListener('DOMContentLoaded', function () {
  var sortableColumns = document.querySelectorAll('.sortable_column');

  sortableColumns.forEach(function (column) {
    var columnId = column.id;

    if (prev_column === columnId) {
      counter++;
    }
    prev_column = columnId

    function buildQueryString() {
      var queryString = Object.keys(params)
        .map(key => encodeURIComponent(key) + '=' + encodeURIComponent(params[key]))
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
      console.log("Event listeners added")
      column.addEventListener('click', function () {
        var listingsTable = document.getElementById('listings-table');
        var queryString = buildQueryString();
        var url = baseUrl + "listings/load_listings_table?" + queryString;
        console.log(url)
        fetch(url)
          .then(response => response.text())
          .then(data => {
            listingsTable.innerHTML = data;
            addEventListeners();
          });
      });
    }

    addEventListeners();
  });
});
