import { createInterface } from "node:readline/promises"; // import the createInterface function from the readline/promises module, which allows us to create a readline interface that returns Promises for asynchronous operations  
import { stdin as input, stdout as output } from "node:process"; // import the stdin and stdout streams from the process module, which represent the standard input and output streams of the Node.js process

// Promises

// Promises are a way to handle asynchronous operations in JavaScript. They represent a value that may not be available yet, but will be resolved at some point in the future. Promises can be in one of three states: pending, fulfilled, or rejected. When a Promise is fulfilled, it means that the asynchronous operation has completed successfully and the value is available. When a Promise is rejected, it means that the asynchronous operation has failed and an error has occurred.

const rl = createInterface({ input, output });

// async is used to declare an asynchronous function, that returns a Promise and allows the use of await within it
async function execute() {
    const name = await rl.question("What is your name? "); // await is used to pause the execution of the async function until the Promise returned by rl.question() is resolved, allowing us to get the user's input before proceeding

    console.log(`Hello, ${name}!`);

    rl.close(); // close the readline interface to free up resources and end the input stream
}

execute();