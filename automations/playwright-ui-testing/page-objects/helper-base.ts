import { expect, Page } from '@playwright/test';


export class HelperBase {
    protected readonly page: Page; 
    //protected means that this variable can be accessed by this class and its subclasses, 
    //but not from outside the class

    constructor(page: Page) {
        this.page = page;
    }

    protected async getBackgroundColorPage() {
        //this method gets the background color of the page
        const layout = await this.page.locator('nb-layout .layout')
        const backgroundColor = await layout.evaluate(element => {
            return window.getComputedStyle(element).backgroundColor
        });
        return backgroundColor;
    }

    protected async verifyBackgroundColorPage(){
        const selectedBackgroundColor = await this.page.getByRole('button').filter({hasText: /Dark|Light|Cosmic|Corporate/}).textContent().then(text => text?.trim())
        const pageBackgroundColor = await this.getBackgroundColorPage()
        if ('Dark' === selectedBackgroundColor) {
            await expect(pageBackgroundColor).toBe('rgb(21, 26, 48)')
        } else if ('Light' === selectedBackgroundColor || 'Corporate' === selectedBackgroundColor) {
            await expect(pageBackgroundColor).toBe('rgb(237, 241, 247)')
        } else if ('Cosmic' === selectedBackgroundColor) {
            await expect(pageBackgroundColor).toBe('rgb(27, 27, 56)')
        }

    }

}