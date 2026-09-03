import { Locator, Page } from '@playwright/test';
import { step } from '../helpers/test-step-decorator';
import { HelperBase } from './helper-base';

export class FormLayoutsPage extends HelperBase {

    constructor(page: Page) {
        super(page);
    }

    @step
    async submitUsingTheGridFomrm(email: string, password: string, optionText: string){
        const usingTheGridForm = this.page.locator('nb-card', { hasText: 'Using the Grid' })
        await usingTheGridForm.getByRole('textbox', { name: 'Email' }).fill(email)
        await usingTheGridForm.getByRole('textbox', { name: 'Password' }).fill(password)

        await usingTheGridForm.getByLabel(optionText).check({ force: true })
        await usingTheGridForm.getByRole('button', { name: 'Sign in' }).click()
    }

    /**
     * This method submits inline form with user full name, email and remember me checkbox option.
     * @param fullName - Valid test user full name (First and last name)
     * @param email - Valid test user email
     * @param rememberMeCheckbox - Pass true to check the "Remember me" checkbox, false to leave it unchecked
     */
    @step
    async submitInlineForm(fullName: string, email: string, rememberMeCheckbox: boolean){
        const inLineForm = this.page.locator('nb-card', { hasText: 'Inline form' })
        await inLineForm.getByRole('textbox', { name: 'Jane Doe' }).fill(fullName)
        await inLineForm.getByRole('textbox', { name: 'Email' }).fill(email)
        if (rememberMeCheckbox) {
            await inLineForm.getByRole('checkbox', { name: 'Remember me' }).check({ force: true })
        }
        await inLineForm.getByRole('button', { name: 'Submit' }).click()
    }
}