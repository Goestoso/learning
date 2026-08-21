// Declarative function
helloOne();
function helloOne(){
    console.log("Hello One");
}

// Anonymous function
var helloTwo = function(){
    console.log("Hello Two");
};
helloTwo();

//ES6 function syntax or arrow function
 var helloThree = () => {
    console.log("Hello Three");
}
helloThree();

// Function with parameters
function helloFour(name, lastName){
    console.log("Hello " + name + " " + lastName);
}
helloFour("Alice", "Smith");

//Function with return value
function multiplyByTwo(num){
    return num * 2;
}
console.log(multiplyByTwo(5));

// Import function from another file
import { printAge } from '../helpers/printHelper.js';
printAge(25);

// import everything from a module
import * as helper from '../helpers/printHelper.js';
helper.printAge(30);