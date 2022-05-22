/**
 * Generate a random number between a minimum and maxinumum value.
 * @param {number} min The minimum number to generate.
 * @param {number} max The maximum number to generate.
 * @returns {number} A random number between min and max.
 */
function random(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1) + min);
}
