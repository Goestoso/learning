// Loops

// statement1 is executed (one time) before the execution of the code block 
// statement2 defines the condition for executing the code block
// statement3 is executed (every time) after the code block has been executed

// for(statement1 ; statement2; statement3) { 
     
//   // code block to be executed
// }

// for loop (for i loop)
for(let i=1; i<6; i++){
    console.log("Hello World! " + i);
}

var cars = ["BMW", "Volvo", "Saab", "Ford"];
// for loop (for of loop)
for(let car of cars){
    console.log(car);
    if(car === "Saab"){
        break;
    }
}

// ES6 syntax for each loop (forEach loop)
cars.forEach( car => {
    console.log(car);
});

// while loop
let j = 0;  

while(j < 5){
    console.log("Hello World! " + j);
    j++;
}