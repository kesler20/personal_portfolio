let nextButton = document.querySelector(".next-btn")
let projectsCards = Array.from(document.querySelector(".projects-cards").children)
// remove the next button from the array
projectsCards.pop()
let currentCardInView = 0

nextButton.addEventListener("click", () => {
  currentCardInView++
  if (currentCardInView != 0) {
    projectsCards[currentCardInView - 1].classList.add("hide")
  }
  if (currentCardInView == projectsCards.length) {
    projectsCards[0].classList.remove("hide")
    currentCardInView = 0
  } else {
    projectsCards[currentCardInView].classList.remove("hide")
  }
})