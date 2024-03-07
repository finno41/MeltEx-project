var listingCards = document.querySelectorAll(".menu-listing-card")
var listingInfoColumn = document.getElementById("listing-info-column")

function highlightListing(listingCards, listingCard) {
  listingCards.forEach(listingCard => {
    listingCard.classList.remove("menu-listing-card-selected")
  })
  listingCard.classList.add("menu-listing-card-selected")
}

listingCards.forEach(listingCard => {
  listingCard.addEventListener('click', function () {
    highlightListing(listingCards, listingCard)
    var listingId = listingCard.id
    const url = `/listings/show_listing/${listingId}`;
    fetch(url)
      .then(response => response.text())
      .then(html => {
        listingInfoColumn.innerHTML = html;
        selectDeselectAssets("round-square-icon", "round-square-icon-selected")
        // ensure that these functions are only called if the listing does not belong to the user
        addEventListenerToRegisterInterest()
        addFetchToInterestSubmit(listingId)
        addEventListenerToCancelButton()
      })
      .catch(error => {
        console.error('Error fetching HTML:', error);
      });
  })
})
