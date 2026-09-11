// @ts-check

/**
 * Generates a random starship registry number.
 *
 * @returns {string} the generated registry number.
 */
export function randomShipRegistryNumber() {
  const minCeiled = Math.ceil(1000);
  const maxFloored = Math.floor(9999);
  const random = Math.floor(Math.random() * (maxFloored - minCeiled + 1)) + minCeiled;
  return `NCC-${random}`;
}

/**
 * Generates a random stardate.
 *
 * @returns {number} a stardate between 41000 (inclusive) and 42000 (exclusive).
 */
export function randomStardate() {
  const random = Math.random() * (42000.0 - 41000.0) + 41000.0;
  return random;
}

/**
 * Generates a random planet class.
 *
 * @returns {string} a one-letter planet class.
 */
export function randomPlanetClass() {
  const planetaryClasses = ["D", "H", "J", "", "L", "M", "N", "R", "T", "Y"]
  const minCeiled = Math.ceil(0);
  const maxFloored = Math.floor(planetaryClasses.length);
  const random = Math.floor(Math.random() * (maxFloored - minCeiled)) + minCeiled;
  return planetaryClasses[random];
}
