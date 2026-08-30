import { expect, test } from "@playwright/test";

test.beforeEach(async ({ page }) => {
    await page.goto('https://playground.bondaracademy.com/');
});

test.describe('Form Layouts page', () => {
    test.beforeEach(async ({ page }) => {
        await page.getByText('Forms').click()
        await page.getByText('Form Layouts').click()
    });

    test('Input fields', async ({ page }) => {
        const usingTheGridEmailInput = page.locator('nb-card', { hasText: "Using the Grid" }).getByRole('textbox', { name: "Email" })
        //clear first and then fill the input value
        await usingTheGridEmailInput.fill('test@test.com')
        //just clear the input value
        await usingTheGridEmailInput.clear()
        //simulates keyboard typing 
        await usingTheGridEmailInput.pressSequentially('test2@test.com', { delay: 500 })

        //extract the value
        const inputValue = await usingTheGridEmailInput.inputValue()

        //assertions
        //full match
        await expect(usingTheGridEmailInput).toHaveValue('test2@tes.com')
        //partial match
        await expect(usingTheGridEmailInput).toHaveValue(/test.com/)
    });


    test('radio buttons', async ({ page }) => {
        const usingTheGridForm = page.locator('nb-card', { hasText: "Using the Grid" })

        //forcing the click on the radio button disconsidering the validations of playwright
        //least recommended
        await usingTheGridForm.getByLabel('Option 1').check({ force: true })
        //most recommended
        await usingTheGridForm.getByRole('radio', { name: "Option 2" }).check({ force: true })

        //dont confuse isChecked with assertion, like the example below:
        const radioStatus = await usingTheGridForm.getByRole('radio', { name: "Option 2" }).isChecked()
        //you get the status and then you validate
        expect(radioStatus).toBeTruthy()

        //instead of getting the status (true or false) you can do the assertion directly as showed below:
        expect(usingTheGridForm.getByRole('radio', { name: "Option 2" })).toBeChecked()
        expect(usingTheGridForm.getByRole('radio', { name: "Option 1" })).not.toBeChecked()
    });

});

test.describe('Modal & Overlays Toastr page', () => {

    test.beforeEach(async ({ page }) => {
        await page.getByText('Modal & Overlays').click()
        await page.getByText('Toastr').click()
    });

    test('checkboxes', async ({ page }) => {

        //click() changes the state of the checkbox (checked to unchecked and vice versa)
        await page.getByRole('checkbox', { name: 'Hide on click' }).click({ force: true })
        //check() changes the state to checked (regardless if it is already checked)
        await page.getByRole('checkbox', { name: 'Hide on click' }).check({ force: true })
        //uncheck() changes the state to unchecked (regardless if it is already unchecked)
        await page.getByRole('checkbox', { name: 'Hide on click' }).uncheck({ force: true })

        //logic to check or uncheck and validate all checkboxes
        const allBoxes = page.getByRole('checkbox')
        for (const box of await allBoxes.all()) {
            await box.uncheck({ force: true })
            await expect(box).not.toBeChecked()
        }
    });

    test('Lists and dropdowns', async ({ page })=> {

        //standard dropdown
        await page.locator('.form-group', {hasText: "Toast type:"}).getByRole('combobox').selectOption('info')
        await expect(page.getByRole('combobox')).toHaveValue('info')

        //custom dropdowns
        await page.locator('.form-group', {hasText: "Position:"}).locator('nb-select').click()
        //option 1
        await page.getByRole('list').getByText('bottom-right').click()
        //option 2
        await page.locator('nb-option', {hasText: "bottom-end"}).click()

        //assertion
        await expect(page.locator('.form-group', {hasText: "Position:"}).locator('nb-select')).toHaveText('bottom-end')

        //looping through the list
        const positionDropDownField = await page.locator('.form-group', {hasText: "Position:"}).locator('nb-select')
        await positionDropDownField.click()
        const allListValues = await page.locator('nb-option').allTextContents()
        for (const listValue of allListValues){
            page.locator('nb-option', {hasText: listValue}).click()
            await expect(page.locator('.form-group', {hasText: "Position:"}).locator('nb-select')).toHaveText(listValue)
            // to continue the loop, you need to click on the dropdown again to open the list
            await positionDropDownField.click() 
        }
    });

});

test('Tooltips', async ({page}) => {
    await page.getByText('Modal & Overlays').click()
    await page.getByText('Tooltip').click()

    await page.getByRole('button', {name: 'Top'}).hover()
    await expect(page.getByRole('tooltip')).toHaveText('This is a tooltip') //you can use a regular locator too
});

test.describe('Tables & Data Smart Table page',  () => {
    test.beforeEach(async ({page}) => {
        await page.getByText('Tables & Data').click()
        await page.getByText('Smart Table').click()
    });

    test('dialog box', async ({page}) => {

        // Register the listener before clicking the delete icon so Playwright is ready to
        // capture the browser dialog as soon as it opens. The callback receives the Dialog
        // object, checks that its message matches the expected confirmation question, and
        // should then accept the dialog so the delete operation can continue.
        page.on('dialog', async dialog => {
            expect(dialog.message()).toEqual('Are you sure you want to delete?')
            await dialog.accept()
        });

        await page.locator('tr', {hasText: 'mdo@gmail.com'}).locator('.nb-trash').click()
        await expect(page.locator('tr', {hasText: 'mdo@gmail.com'})).not.toBeVisible()
    });

});


