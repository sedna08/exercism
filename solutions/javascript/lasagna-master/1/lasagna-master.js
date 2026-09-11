/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */

export function cookingStatus(remainingTime) {
  if(remainingTime === 0 )
    return 'Lasagna is done.';
  else if ( remainingTime !== 0 && remainingTime !== undefined && remainingTime !== null)
    return 'Not done, please wait.';
  else 
    return 'You forgot to set the timer.';
}

export function preparationTime(layers, averagePreparationTime) {
  if(averagePreparationTime !== undefined )
    return layers.length * averagePreparationTime;
  else
    return layers.length * 2;
}

export function quantities(layers) {
  let countNoodles = 0;
  let countSauce = 0;
  for (const item of layers) {
    if (item === "noodles") {
      countNoodles++;
    }
    else if (item === "sauce") {
      countSauce++;
    }
  }
  return {noodles: (countNoodles * 50), sauce: (countSauce * 0.2)};
}

export function addSecretIngredient(friendList, ownList) {
  ownList.push(friendList[friendList.length - 1]);
}

export function scaleRecipe(recipe, portions) {
  const needAmounts = {};
  const portionMultiplier = portions / 2;
  for(let key in recipe) {
    needAmounts[key] = recipe[key] * portionMultiplier;
  }
  return needAmounts;
}