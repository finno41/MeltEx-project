var listingCards = document.querySelectorAll(".menu-listing-card")

console.log(listingCards)

listingCards.forEach(listingCard => {
  listingCard.addEventListener('click', function () {
    listingCards.forEach(listingCard => {
      listingCard.classList.remove("menu-listing-card-selected")
    })
    listingCard.classList.add("menu-listing-card-selected")
  })
})
