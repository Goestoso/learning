// TypeScript is a typed superset of JavaScript that compiles to plain JavaScript. It adds optional static typing, classes, and interfaces to JavaScript. TypeScript is designed for the development of large applications and transcompiles to JavaScript

var customerFirstName: string = "John";
var customerLastName: string = "Doe";
var customerAge: number = 30;

// customerFirstName = 100; // Error: Type 'number' is not assignable to type 'string'.

// type is inferred from the value assigned to the variable
type Customer = {firstName: string, lastName: string, active: boolean}; // type creates a new type called Customer with the specified properties and their types

var firstCustomer: Customer = {
    firstName: "John",
    lastName: "Doe",
    active: true
}