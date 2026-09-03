import { Locator, Page } from '@playwright/test';
import { step } from '../helpers/test-step-decorator';
import { HelperBase } from './helper-base';

export class NavigationPage extends HelperBase {

    //Locators in Page Objects - recommended by Playwright, but you can use you own approach too
    readonly formLayoutsMenu: Locator;
    readonly datePickerMenu: Locator;
    readonly toasterMenu: Locator;
    readonly tooltipMenu: Locator;
    readonly smartTableMenu: Locator;

    // A constructor is a block of code that executes as a first thing when you initialize an object of a class
    //we need it pass the page instance to the class so we can use it in the methods of the class
    constructor(page: Page) {
        super(page);
        this.smartTableMenu = page.getByText('Smart Table')
        this.formLayoutsMenu = page.getByText('Form Layouts')
        this.datePickerMenu = page.getByText('Datepicker')
        this.toasterMenu = page.getByText('Toastr')
        this.tooltipMenu = page.getByText('Tooltip')
    }

    @step
    async formLayoutsPage(){
        await this.selectGroupMenuItem('Forms') //you always use this. to access the instance variables and methods of the class
        await this.formLayoutsMenu.click()
        await this.verifyBackgroundColorPage() //inherited from HelperBase class
    }

    @step
    async datePickerPage(){
        await this.selectGroupMenuItem('Forms')
        await this.datePickerMenu.click()
        await this.verifyBackgroundColorPage()
    }

    @step
    async toasterPage(){
        await this.selectGroupMenuItem('Modal & Overlays')
        await this.toasterMenu.click()
        await this.verifyBackgroundColorPage()
    }

    @step
    async tooltipPage(){
        await this.selectGroupMenuItem('Modal & Overlays')
        await this.tooltipMenu.click()
        await this.verifyBackgroundColorPage()

    }

    @step
    async smartTablePage(){
        await this.selectGroupMenuItem('Tables & Data')
        await this.smartTableMenu.click()
        await this.verifyBackgroundColorPage()
    }

    private async selectGroupMenuItem(groupMenuTitle: string) {
        const groupMenuItem = this.page.getByTitle(groupMenuTitle)
        const expandedState = await groupMenuItem.getAttribute('aria-expanded')
        if (expandedState === "false") {
            await groupMenuItem.click()
        } 
    }


}