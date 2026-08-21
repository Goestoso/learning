// Logical Operators
// Logical "AND"
console.log(true && true);   // true
console.log(true && false);  // false

// Logical "OR"
console.log(true || false);  // true
console.log(false || false); // false

var ageIsMoreThan18 = true;
var hasParentalConsent = false;

var elibilityForDriving = ageIsMoreThan18 && hasParentalConsent;
console.log('This customer is eligible for driving: ' + elibilityForDriving); // false
console.log(`This customer is eligible for voting: ${ageIsMoreThan18 || hasParentalConsent}`); // true

// Logical "NOT"
console.log(!true);  // false
console.log(6 !== 10); // true