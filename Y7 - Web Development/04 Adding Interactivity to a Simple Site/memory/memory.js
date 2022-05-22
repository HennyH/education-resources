/**
 * Shuffles an array like a deck of cards.
 * @param {Array} array The array to shuffle.
 */
function shuffle(array) {
  var currentIndex = array.length,
    temporaryValue,
    randomIndex;

  while (currentIndex !== 0) {
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }
}

/**
 * Generate a random number between a minimum and maximum value.
 * @param {number} min The minimum number that can be generated.
 * @param {number} max The maximum number that can be generated.
 */
function random(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1) + min);
}

/**
 * Choose a number of items randomly from an array.
 * @param {Array} array The array to choose items from.
 * @param {number} n The number of items to choose.
 */
function choose(array, n) {
  array = [...array];
  shuffle(array);
  return array.filter((_, i) => i < n);
}

/**
 * Returns an array of strings which will be used as face values for cards.
 */
function getPossibleCardFaceValues() {
  return [
    "🍃", "🍂", "🍁", "🍀", "🌿", "🌾", "🌵", "🌴", "🌳", "🌱",
    "🍎", "☘", "🥀", "🌷", "🌼", "🌻", "🌺", "🌹", "🏵", "🌸", "💐",
    "🍋", "🥦", "🍄", "🌶", "🧅", "🧄", "🍒", "🍓", "🍅", "🍏", "🍉",
  ];
}

/**
 * Remove all cards from a game board.
 * @param {HTMLElement} board The board HTML element which contains the cards as children.
 */
function clearCardsFromBoard(board) {
  const cards = board.querySelectorAll(".card");
  for (const card of cards) {
    board.removeChild(card);
  }
}

/**
 * Create a `div.card` element which has a given facevalue.
 * @param {string} faceValue The string to show on the card's face.
 */
function createCard(faceValue) {
  const cardElement = document.createElement("div");
  cardElement.classList.add("card");
  cardElement.classList.add("face-down");
  cardElement.innerText = faceValue;
  return cardElement;
}

/**
 * Flip a card over.
 * @param {HTMLElement} card The card to flip.
 */
function flipCard(card) {
  const isFaceUp = isCardFaceUp(card);
  if (isFaceUp) {
    card.classList.remove("face-up");
    card.classList.add("face-down");
  } else {
    card.classList.remove("face-down");
    card.classList.add("face-up");
  }
}

/**
 * Determines if a card is face-up on the board.
 * @param {HTMLElement} card 
 */
function isCardFaceUp(card) {
  return card.classList.contains("face-up");
}

/**
 * Returns true if the two cards are considered a match.
 * @param {HTMLElement} firstCard The first flipped card.
 * @param {HTMLElement} secondCard The second flipped card.
 */
function isCardMatch(firstCard, secondCard) {
  console.log(firstCard, secondCard);
  return firstCard.textContent === secondCard.textContent;
}

/**
 * Start a game of memory.
 * @param {HTMLElement} board The element in which to render the board.
 * @param {number} numberOfPairs The number of pairs to place on the board.
 */
function startGame(board, numberOfPairs) {
  /* randomly choose the face values for our pairs of cards */
  const possibleFaceValues = getPossibleCardFaceValues();
  const faceValues = choose(possibleFaceValues, numberOfPairs);

  /* create a two card elements for each face value - so we have pairs! */
  const cards = [];
  for (const faceValue of faceValues) {
    cards.push(createCard(faceValue), createCard(faceValue));
  }

  /* define an event handler for when a card gets clicked */
  let firstCard = undefined;
  let secondCard = undefined;

  /**
   * Handle a card being clicked.
   * @param {MouseEvent} event 
   */
  function handleCardClicked(event) {
    event.preventDefault();
    event.stopPropagation();

    const card = event.target;

    /* We cannot flip a card that is face up! */
    if (isCardFaceUp(card)) {
      return;
    }

    /* We cannot select the same card twice! */
    if (firstCard !== undefined && firstCard === card) {
      return;
    }

    /* If we've selected two cards already, dont let us select another
     * until they either got matched or flipped back over - in both cases
     * the `firstCard` and `secondCard` would've been set back to undefined.
     */
    if (firstCard !== undefined && secondCard !== undefined) {
      return;
    }

    /* Flip the selected card so it's face up */
    flipCard(card);

    /* Depending on if we've selected a card before or not
     * update the correct variable.
     */
    if (firstCard === undefined) {
      firstCard = card;
    } else {
      secondCard = card;
    }

    /* If we've flipped face up two cards, we need to check if they match,
     * and then reset our selection.
     */
    if (firstCard !== undefined && secondCard !== undefined) {
      /* We put the following code inside a `setTimeouts` so that we delay
       * running it for a short while, if we didn't then the second selected
       * card (which we just flipped) would suddenly be flipped back! This
       * looks very weird... not good!
       */
      if (isCardMatch(firstCard, secondCard)) {
        setTimeout(() => {
          firstCard.classList.add("matched");
          secondCard.classList.add("matched");
          firstCard = undefined;
          secondCard = undefined;
        }, 200)
      } else {
        setTimeout(() => {
          flipCard(firstCard);
          flipCard(secondCard);
          firstCard = undefined;
          secondCard = undefined;
        }, 500)
      }
    }
  }

  /* After having just defined our `handleCardClicked` function we
   * want to "attach" it to every card so it gets called when
   * we click any card.
   */
  for (const card of cards) {
    card.addEventListener("click", handleCardClicked);
  }

  /* shuffle our cards and add them to the board, otherwise all the pairs
   * would appear alongside each other!
   */
  shuffle(cards);
  for (const card of cards) {
    board.appendChild(card);
  }
}

const board = document.getElementById("board");
startGame(board, 10);
