import { expect, test } from "@playwright/test";

test('Input fields', { tag: ['@smoke', '@fields'] }, async ({ page }, testInfo) => {

    await page.goto('/')
    if(testInfo.project.name == 'mobile-test') {
        await page.locator('.sidebar-toggle').click()
    }
    await page.getByText('Forms').click()
    await page.getByText('Form Layouts').click()
    if(testInfo.project.name == 'mobile-test') {
        await page.locator('.sidebar-toggle').click()
    }

    const usingTheGridEmailInput = page.locator('nb-card', { hasText: "Using the Grid" }).getByRole('textbox', { name: "Email" })
    await usingTheGridEmailInput.pressSequentially('test2@test.com', { delay: 100 })
});