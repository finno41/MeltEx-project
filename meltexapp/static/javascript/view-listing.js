var popupLinks = document.querySelectorAll(".popup-link");


popupLinks.forEach(popupLink => {
  console.log(popupLink)
  const listingId = popupLink.id;
  popupLink.addEventListener("click", function (event) {
    event.preventDefault();
    const url = `/listings/show_listing/${listingId}`;
    fetch(url)
      .then(response => response.text())
      .then(html => {
        document.getElementById("view-listing-content").innerHTML = html
      })
      .catch(error => {
        console.error('Error fetching HTML:', error);
      });
  })
})
