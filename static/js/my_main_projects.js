const projectsCards = Array.from(
  document.querySelector(".projects-cards").children
);

// if mobile view hide the other two starting cards
if (window.innerWidth <= 560) {
  projectsCards[1].classList.add("hide");
  projectsCards[2].classList.add("hide");
}

// remove the next button from the array
const nextButton = projectsCards.pop();
const nextButtonIcon = nextButton.children.item(0);
let nextButtonIconFlipped = true;

let currentCardInView = 0;

nextButton.addEventListener("click", () => {
  // if the view is mobile change one card at a time
  if (window.innerWidth <= 360) {
    currentCardInView++;
    if (currentCardInView != 0) {
      projectsCards[currentCardInView - 1].classList.add("hide");
    }
    if (currentCardInView == projectsCards.length) {
      // if the current card in view corresponds to the last one
      // uncover the first element to restart, (the last one will be hidden from the line above)
      projectsCards[0].classList.remove("hide");
      currentCardInView = 0;
      // flip the arrow
      nextButtonIcon.classList.toggle("flip-right", nextButtonIconFlipped);
      nextButtonIcon.classList.toggle("flip-left", !nextButtonIconFlipped);
      nextButtonIconFlipped = !nextButtonIconFlipped;
    } else {
      projectsCards[currentCardInView].classList.remove("hide");
    }
  } else {
    // flip the arrow
    nextButtonIcon.classList.toggle("flip-right", nextButtonIconFlipped);
    nextButtonIcon.classList.toggle("flip-left", !nextButtonIconFlipped);
    nextButtonIconFlipped = !nextButtonIconFlipped;
    if (currentCardInView == 0) {
      projectsCards[0].classList.add("hide");
      projectsCards[1].classList.add("hide");
      projectsCards[2].classList.add("hide");
      projectsCards[3].classList.remove("hide");
      projectsCards[4].classList.remove("hide");
      projectsCards[5].classList.remove("hide");
      currentCardInView = 1;
    } else {
      projectsCards[0].classList.remove("hide");
      projectsCards[1].classList.remove("hide");
      projectsCards[2].classList.remove("hide");
      projectsCards[3].classList.add("hide");
      projectsCards[4].classList.add("hide");
      projectsCards[5].classList.add("hide");
      currentCardInView = 0;
    }
  }
});
