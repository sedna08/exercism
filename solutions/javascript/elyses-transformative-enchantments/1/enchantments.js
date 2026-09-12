// @ts-check

/**
 * Double every card in the deck.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} deck with every card doubled
 */
export function seeingDouble(deck) {
  const newDeck = deck.map((value) => value * 2);
  return newDeck;
}

/**
 *  Creates triplicates of every 3 found in the deck.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} deck with triplicate 3s
 */
export function threeOfEachThree(deck) {
  const newDeck = deck.flatMap((value) => {
    if(value === 3)
      return [3, 3, 3];
    else
      return value;
  });
  return newDeck;
}

/**
 * Extracts the middle two cards from a deck.
 * Assumes a deck is always 10 cards.
 *
 * @param {number[]} deck of 10 cards
 *
 * @returns {number[]} deck with only two middle cards
 */
export function middleTwo(deck) {
  const middleCards = deck.splice(4,2);
  return middleCards;
}

/**
 * Moves the outside two cards to the middle.
 *
 * @param {number[]} deck with even number of cards
 *
 * @returns {number[]} transformed deck
 */

export function sandwichTrick(deck) {
  // 1. Separate the first and last cards using built-in array methods
  const first = deck.shift();
  const last = deck.pop();
  
  // 2. Combine and reverse them into our sandwich meat array: [last, first]
  const sandwichMeat = [last, first];
  
  // 3. Find the exact middle index of the remaining deck
  const middleIndex = Math.floor(deck.length / 2);
  
  // 4. Use splice to inject the reversed cards. 
  // We use ...sandwichMeat so they insert as individual cards, not a nested array.
  deck.splice(middleIndex, 0, ...sandwichMeat);
  
  // 5. Return the modified deck
  return deck;
}

/**
 * Removes every card from the deck except 2s.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} deck with only 2s
 */
export function twoIsSpecial(deck) {
  const newDeck = deck.filter((value) => value === 2);
  return newDeck;
}

/**
 * Returns a perfectly order deck from lowest to highest.
 *
 * @param {number[]} deck shuffled deck
 *
 * @returns {number[]} ordered deck
 */
export function perfectlyOrdered(deck) {
  return deck.sort((a, b) => a - b);
}

/**
 * Reorders the deck so that the top card ends up at the bottom.
 *
 * @param {number[]} deck
 *
 * @returns {number[]} reordered deck
 */
export function reorder(deck) {
  return deck.reverse();
}
