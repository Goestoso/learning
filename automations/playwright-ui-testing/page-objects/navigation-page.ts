import { Page } from '@playwright/test';

export class NavigationPage {

    readonly page: Page; //something that should only be consulted outside the class and only changed by the class itself.

    // A constructor is a block of code that executes as a first thing when you initialize an object of a class
    //we need it pass the page instance to the class so we can use it in the methods of the class
    constructor(page: Page) {
        this.page = page //this.page is the instance variable that will hold the page object passed to the constructor
    }

    async formLayoutsPage(){
        await this.selectGroupMenuItem('Forms') //you always use this. to access the instance variables and methods of the class
        await this.page.getByText('Form Layouts').click()
    }

    async datePickerPage(){
        await this.selectGroupMenuItem('Forms')
        await this.page.getByText('Datepicker').click()
    }
    
    async toasterPage(){
        await this.selectGroupMenuItem('Modal & Overlays')
        await this.page.getByText('Toastr').click()
    }

    async tooltipPage(){
        await this.selectGroupMenuItem('Modal & Overlays')
        await this.page.getByText('Tooltip').click()

    }

    async smartTablePage(){
        await this.selectGroupMenuItem('Tables & Data')
        await this.page.getByText('Smart Table').click()
    }

    private async selectGroupMenuItem(groupMenuTitle: string) {
        const groupMenuItem = this.page.getByTitle(groupMenuTitle)
        const expandedState = await groupMenuItem.getAttribute('aria-expanded')
        if (expandedState === "false") {
            await groupMenuItem.click()
        } 
    }


}