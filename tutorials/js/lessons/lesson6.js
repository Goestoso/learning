//Conditional Statements

// if (condition) {
//   // code to be executed if condition is true
// } else {
//     // code to be executed if condition is false
// }

// If hour betweem 6am and 12pm, say "Good morning!"
// If hour between 12 and 18 print "Good afternoon!"
// Otherwise say "Good evening!"

var hour = 14
if (hour >= 6 && hour < 12) {
  console.log("Good morning!");
} else if (hour >= 12 && hour < 18) {
  console.log("Good afternoon!");
} else {
  console.log("Good evening!");
}

var ageIsMoreThan18 = true;
var isUSCitizen = false;

if (ageIsMoreThan18 && isUSCitizen) {  
    console.log("This customer is eligible for voting");
} else {
    console.log("This customer is not eligible for voting");
}