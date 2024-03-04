var listingCards = document.querySelectorAll(".menu-listing-card")

console.log(listingCards)

listingCards.forEach(listingCard => {
  listingCard.addEventListener('click', function () {
    listingCard.classList.add("menu-listing-card-selected")
  })
})
