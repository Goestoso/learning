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

    test('Lists and dropdowns', async ({ page }) => {

        //standard dropdown
        await page.locator('.form-group', { hasText: "Toast type:" }).getByRole('combobox').selectOption('info')
        await expect(page.getByRole('combobox')).toHaveValue('info')

        //custom dropdowns
        await page.locator('.form-group', { hasText: "Position:" }).locator('nb-select').click()
        //option 1
        await page.getByRole('list').getByText('bottom-right').click()
        //option 2
        await page.locator('nb-option', { hasText: "bottom-end" }).click()

        //assertion
        await expect(page.locator('.form-group', { hasText: "Position:" }).locator('nb-select')).toHaveText('bottom-end')

        //looping through the list
        const positionDropDownField = await page.locator('.form-group', { hasText: "Position:" }).locator('nb-select')
        await positionDropDownField.click()
        const allListValues = await page.locator('nb-option').allTextContents()
        for (const listValue of allListValues) {
            page.locator('nb-option', { hasText: listValue }).click()
            await expect(page.locator('.form-group', { hasText: "Position:" }).locator('nb-select')).toHaveText(listValue)
            // to continue the loop, you need to click on the dropdown again to open the list
            await positionDropDownField.click()
        }
    });

});

test('Tooltips', async ({ page }) => {
    await page.getByText('Modal & Overlays').click()
    await page.getByText('Tooltip').click()

    await page.getByRole('button', { name: 'Top' }).hover()
    await expect(page.getByRole('tooltip')).toHaveText('This is a tooltip') //you can use a regular locator too
});

test.describe('Tables & Data Smart Table page', () => {
    test.beforeEach(async ({ page }) => {
        await page.getByText('Tables & Data').click()
        await page.getByText('Smart Table').click()
    });

    test('dialog box', async ({ page }) => {

        // Register the listener before clicking the delete icon so Playwright is ready to
        // capture the browser dialog as soon as it opens. The callback receives the Dialog
        // object, checks that its message matches the expected confirmation question, and
        // should then accept the dialog so the delete operation can continue.
        page.on('dialog', async dialog => {
            expect(dialog.message()).toEqual('Are you sure you want to delete?')
            await dialog.accept()
        });

        await page.locator('tr', { hasText: 'mdo@gmail.com' }).locator('.nb-trash').click()
        await expect(page.locator('tr', { hasText: 'mdo@gmail.com' })).not.toBeVisible()
    });

    test('web tables', async ({ page }) => {
        //1 how to select row by any visibile text
        const tableRowByEmail = page.getByRole('row', { name: "twitter@outlook.com" })
        await tableRowByEmail.locator('.nb-edit').click()
        await tableRowByEmail.getByPlaceholder('Age').fill('35')
        await tableRowByEmail.locator('.nb-checkmark').click()
        await expect(tableRowByEmail.locator('td').last()).toHaveText('35')

        //2 how to get a row by a specific column value
        const tableRowById = page.getByRole('row').filter({ has: page.getByRole('cell').nth(1).getByText('10') })
        await tableRowById.locator('.nb-edit').click()
        //you can no longer use the tableRowById locator because now it has only input fields and not text values
        await page.locator('tbody').getByPlaceholder('E-mail').fill('test@test.com')
        await page.locator('tbody').locator('.nb-checkmark').click()
        await expect(tableRowById.locator('td').nth(5)).toHaveText('test@test.com')

        //3 loop thorugh table rows
        const ages = ["20", "30", "40", "200"]

        for (let age of ages) {
            await page.getByPlaceholder('Age').fill(age)

            if (age == "200") {
                await expect(page.locator('tbody')).toContainText('No data found')
            } else {
                //there is a delay just after you trype the filter, so you need to wait the table be updated
                //and one way to turn araound this is making an assertion
                await expect(page.locator('tbody tr').first().locator('td').last()).toHaveText(age)
                const allTableRows = await page.locator('tbody tr').all()
                for (let row of allTableRows) {
                    await expect(row.locator('td').last()).toHaveText(age)
                }
            }
        }
    });

});

test('date picker', async ({page}) => {
    await page.getByText('Forms').click()
    await page.getByText('Datepicker').click()

    const calendarInputField = page.getByPlaceholder('Form Picker')
    await calendarInputField.click()

    //it's a good idea to use Date() when you want to validate current or future dates
    const date = new Date();
    date.setDate(date.getDate()+100)
    const expectedDay = date.getDate().toString()
    const expectedMonth = date.toLocaleString('En-US', {month: 'short'})
    const expectedMonthLong = date.toLocaleString('En-US', {month: 'long'})
    const expectedYear = date.getFullYear()
    const expectedDate = `${expectedMonth} ${expectedDay}, ${expectedYear}`

    //if the future date falls in future months
    let currentMonthAndYear = await page.locator('nb-calendar-view-mode').textContent()
    const expectedMonthAndYear = `${expectedMonthLong} ${expectedYear}`
    while(!currentMonthAndYear?.includes(expectedMonthAndYear)){
        await page.locator('.next-month').click()
        currentMonthAndYear = await page.locator('nb-calendar-view-mode').textContent()
    }

    await page.locator('.day-cell:not(.bounding-month)').getByText(expectedDay, {exact: true}).click()
    await expect(calendarInputField).toHaveValue(expectedDate)
});

test('sliders', async ({page}) => {
    //1 setting the attribute values
    const tempGauge = page.locator('[tabtitle="Temperature"] ngx-temperature-dragger circle')
    await tempGauge.evaluate( element =>  {
        element.setAttribute('cx', '232.630')
        element.setAttribute('cy', '232.630')
    });
    await tempGauge.click()

    //2 mouse movement
    const tempBox = page.locator('[tabtitle="Temperature"] ngx-temperature-dragger')
    await tempBox.scrollIntoViewIfNeeded()
    //create coordinates within the tempBox (pixels are generally used as the unit of measurement)
    //y ^
    //  |
    //  |
    //x --------------------->
    const box = await tempBox.boundingBox()
    //to find the center position of the tempBox
    const x = box?.x + box?.width / 2
    const y = box?.y + box?.height / 2

    await page.mouse.move(x, y)
    await page.mouse.down() //presses and holds down the mouse button
    await page.mouse.move(x+100, y)
    await page.mouse.move(x+100, y+100)
    await page.mouse.up() //releases the mouse button
    await expect(tempBox).toContainText('30')
});

test('iFrames', async ({ page }) => { //An iframe is a web page embedded within another web page
    await page.getByText('Modal & Overlays').click()
    await page.getByText('Dialog').click()

    const frameLocator = page.frameLocator('[data-cy="esc-close-iframe"]')

    await frameLocator.getByRole('button', {name: "Open Dialog with esc close"}).click()

});

test('Drag & Drop', async ({page}) => {
    await page.getByText('Extra Components').click()
    await page.getByText('Drag & Drop').click()

    //option 1 - using playwright method
    await page.getByText('Clean my room').dragTo(page.locator('#drop-list'))

    //option 2 - simulate the mouse movement
    await page.getByText('Get groceries').hover()
    await page.mouse.down() //presses and holds down the mouse button
    await page.locator('#drop-list').hover()
    await page.mouse.up() //releases the mouse button
});
