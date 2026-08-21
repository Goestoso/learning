// 1.Hello World
console.log("Hello World!")

// Variables
var firstName = "John" // var is function scoped
let lastName = "Smith" // let is block scoped
console.log(firstName)

var age, dateOfBirth, sex

age = "5"
age = 5
sex = "Male"
console.log(age)
age = "6"
console.log(age)

//constants (constant cannot be created without a value)
const occupation = "Engineer" // const is block scoped and cannot be reassigned
// occupation = "driver" // This will cause an error
console.log(occupation)

// Data Types
var name = "David" // String is a sequence of characters
var ageOfPerson = 25 // Number is a numeric data type
var isMarried = false // Boolean is a data type that can be either true or false
var nullValue = null // Null is a data type that represents the absence of a value
var any = undefined // Undefined is a data type that represents a variable that has not been assigned a value