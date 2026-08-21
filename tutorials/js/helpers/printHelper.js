
export function printAge(age) {
    console.log(age);
}

export class CustomerDetails {
    printFirstName(firstName) {
        console.log(firstName);
    }

    /**
     * This method prints the last name of the customer.
     * @param {string} lastName 
     */
    printLastName(lastName) {
        console.log(lastName);
    }
}

class Potato {
    constructor() {
        console.log("Potato class constructor");
    }
    countPotates() {
        console.log("Counting potatoes");
    }
}

export const potato = new Potato();