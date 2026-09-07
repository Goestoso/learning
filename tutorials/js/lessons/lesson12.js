// Callbacks

// Callbacks are functions that are passed as arguments to other functions and are executed after some operation has been completed. They are commonly used in asynchronous programming to handle tasks that take time to complete, such as reading files, making network requests, or performing database operations.

import { createInterface } from "node:readline"; // import the createInterface function from the readline module, which allows us to create a readline interface that can read input from the standard input stream and write output to the standard output stream using callbacks
import { stdin as input, stdout as output } from "node:process"; // import the stdin and stdout streams from the process module, which represent the standard input and output streams of the Node.js process

const terminal = createInterface({ input, output }); // create a readline interface that reads input from the standard input stream and writes output to the standard output stream

terminal.question("What is your name? \n", (name) => {   // terminal.question() is a method that takes a question string and a callback function as arguments. The callback function is executed after the user provides input, and the input is passed as an argument to the callback function
  terminal.question("How old are you? \n", (age) => { // nested terminal.question() to ask the user for their age after they have provided their name. The callback function is executed after the user provides input, and the input is passed as an argument to the callback function
    console.log(`Hello, ${name}! You are ${age} years old.`);  // log the user's input to the console using template literals to interpolate the value of the name variable into the string
    terminal.close(); // close the readline interface to free up resources and end the input stream
  });
});