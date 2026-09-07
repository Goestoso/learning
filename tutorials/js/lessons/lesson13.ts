// try-catch-finally

import { createInterface } from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";

const terminal = createInterface({ input, output });
var tryAgain = true;

// try catch block to handle errors and ensure the terminal is closed properly

async function calculateSum() {
  while (tryAgain) { // loop to allow the user to try again if an error occurs
    try { // try block to catch any errors that may occur during execution

      const primeiroInput = await terminal.question("First number: ");
      const segundoInput = await terminal.question("Second number: ");

      const firstNumber = Number(primeiroInput);
      const secondNumber = Number(segundoInput);

      if (Number.isNaN(firstNumber) || Number.isNaN(secondNumber)) {
        throw new Error("Invalid input: Please enter valid numbers."); // throw an error if the input is not a valid number
      } else {
        console.log(`Result: ${firstNumber + secondNumber}`);
        tryAgain = false; // exit the loop if the input is valid
      }

    } catch (error) { // catch block to handle any errors that may occur during execution 
      console.error(error instanceof Error ? error.message : error); // log the error message to the console
    } finally { // finally block to ensure the terminal is closed properly // finally is executed regardless of whether an error occurred or not
      
      !tryAgain ? terminal.close() : null; // close the terminal if the user does not want to try again
    }
  }
}

calculateSum();

