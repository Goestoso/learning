import { test } from '../fixture';
import { faker } from '@faker-js/faker'; //to  generate random test data
import * as path from 'node:path';

test('Navigate to form layouts page', async ({ pom }) => {

    await pom.navigateTo.formLayoutsPage()
    await pom.navigateTo.datePickerPage()
    await pom.navigateTo.toasterPage()
    await pom.navigateTo.tooltipPage()
    await pom.navigateTo.smartTablePage()
});

test('Parametrized page object methods', async ({ pom }) =>  {

    const randomFullName = faker.person.fullName()
    const randomEmail = faker.internet.email({provider: "test.com"})

    await pom.navigateTo.formLayoutsPage()
    await pom.formLayoutsPage.submitUsingTheGridFomrm(randomEmail, process.env.TEST_USER_PASSWORD!, process.env.TEST_USER_OPTION!)

    // await page.waitForTimeout(500)
    // await page.screenshot({
    // path: path.resolve(__dirname, '../screenshots/formlayoutsPage.png')}); //the screenshot will be stored in the screenshots directory (inside the playwright-ui-testing project)
    // const formLayoutPageBuffer = await page.screenshot()
    // console.log(formLayoutPageBuffer.toString('base64')) //to get the image data

    await pom.formLayoutsPage.submitInlineForm(randomFullName, randomEmail, true)
    // await page.locator('nb-card', { hasText: 'Inline form' }).screenshot({
    // path: path.resolve(__dirname, '../screenshots/InlineForm.png')}) //screenshot will be applied only for this locator
    
    await pom.navigateTo.datePickerPage()
    await pom.datepickerPage.selectCommonDatepickerDateFromToday(5)
    await pom.datepickerPage.selectDatePickerWithRangeFromToday(7, 20)
});