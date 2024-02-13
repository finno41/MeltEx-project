var counter = 0;
var prev_column = null;
var baseUrl = window.location.origin + "/"
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
      prev_column = columnId
      urlString = window.location.href;
      url = new URL(urlString);
      queryString = new URLSearchParams(url.search);
      if (counter % 3 !== 2) {
        queryString += "&" + encodeURIComponent("sort") + "=" + encodeURIComponent(columnId);
        sortIcon = '<i class="fa-solid fa-sort-down"></i>'
      }
      if (counter % 3 === 0) {
        queryString += "&" + encodeURIComponent("ascending") + "=" + encodeURIComponent("true");
        sortIcon = '<i class="fa-solid fa-sort-up"></i>';
      }
      if (counter % 3 === 2) {
        sortIcon = '';
      }
      return queryString;
    }

    function addEventListeners() {
      column.addEventListener('click', function () {
        var listingsTable = document.getElementById('listings-table');
        var queryString = buildQueryString();
        var url = baseUrl + `listings/load_listings_table/${listingsType}?${queryString}`;
        fetch(url)
          .then(response => response.text())
          .then(data => {
            listingsTable.innerHTML = data;
            var sortableColumns = document.querySelectorAll('.sortable_column');
            addColumnsEventListener(sortableColumns);
            var sortedColumn = document.querySelector(`.sortable_column#${columnId}`);
            sortedColumn.innerHTML += ` ${sortIcon}`;
          })
      });
    }
    addEventListeners();
  });
};
