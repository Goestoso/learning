//objects

var customer = {
    name: "John",
    age: 30,
    cars: ["BMW", "Audi", "Mercedes"]
}

console.log(customer.name) // dot notation
console.log(customer['age']) // bracket notation
console.log(customer.cars) // accessing the cars array
console.log(customer.cars[1]) // accessing the second element of the cars array

customer.name = "David" // updating the value of name property
console.log(customer.name)

customer['age'] = 35 // updating the value of age property
console.log(customer['age'])

console.log(`Customer: ${customer.name}, Age: ${customer['age']}, Cars: ${customer.cars.join(", ")}`) // using interpolation to print customer details

//arrays
var cars = ["BMW", "Audi", "Mercedes"]
console.log(cars[0]) // accessing the first element
console.log(cars.length) // getting the length of the array
cars[0] = "Toyota" // updating the first element
console.log(cars[0])