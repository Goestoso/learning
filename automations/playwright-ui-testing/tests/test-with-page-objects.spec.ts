import { test } from '@playwright/test';
import { PageManager } from '../page-objects/page-manager';

test.beforeEach(async ({ page}) => {
    await page.goto('https://playground.bondaracademy.com/');
});

test('Navigate to form layouts page', async ({ page}) => {
    const pom = new PageManager(page)
    await pom.navigateTo.formLayoutsPage()
    await pom.navigateTo.datePickerPage()
    await pom.navigateTo.toasterPage()
    await pom.navigateTo.tooltipPage()
    await pom.navigateTo.smartTablePage()
});

test('Parametrized page object methods', async ({ page}) =>  {
    const pom = new PageManager(page)
    await pom.navigateTo.formLayoutsPage()
    await pom.formLayoutsPage.submitUsingTheGridFomrm('test@example.com', 'password123', 'Option 1')
    await pom.formLayoutsPage.submitInlineForm('Patton Dog', 'john@example.com', true)
    await pom.navigateTo.datePickerPage()
    await pom.datepickerPage.selectCommonDatepickerDateFromToday(5)
    await pom.datepickerPage.selectDatePickerWithRangeFromToday(7, 20)
});