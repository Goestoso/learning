//Concatenation and Interpolation
var price = 50
var itemName = "Cup"
var messageToPrint = "The price for your " + itemName + " is " + price + " dollars" // concatenation
console.log(messageToPrint)
var messageToPrint2 = `The price for your ${itemName} is ${price} dollars` // interpolation
console.log(messageToPrint2)