//
// This is only a SKELETON file for the 'Line Up' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const format = (name, position) => {
  const number = Math.abs(Math.floor(position));
  const lastTwoDigits = number % 100;
  if (lastTwoDigits >= 11 && lastTwoDigits <= 13) {
    return `${name}, you are the ${position}th customer we serve today. Thank you!`
  }

  const lastDigit = number % 10;
  switch(lastDigit) {
    case 1:
      return `${name}, you are the ${position}st customer we serve today. Thank you!` 
      break;
    case 2:
      return `${name}, you are the ${position}nd customer we serve today. Thank you!` 
      break;
    case 3:
      return `${name}, you are the ${position}rd customer we serve today. Thank you!` 
      break;
    default: 
      return `${name}, you are the ${position}th customer we serve today. Thank you!` 
  }
};
