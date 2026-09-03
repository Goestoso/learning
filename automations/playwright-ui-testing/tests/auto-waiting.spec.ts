import {expect, test} from '@playwright/test'

test.beforeEach(async ({page}, testInfo) => {
    await page.goto('https://playground.bondaracademy.com/');
    await page.getByText('Modal & Overlays').click();
    await page.getByText('Dialog').click();
    testInfo.setTimeout(testInfo.timeout + 3000) // Get the current timeout and increase it by three seconds.
});

test('Auto waiting', async ({page}) => {

    // Locate the card that contains the controls for opening a dialog after a delay.
    // hasText narrows the search to the <nb-card> whose text includes "Open Dialog With Delay".
    const dialogWithDelayForm = page.locator('nb-card', { hasText: 'Open Dialog With Delay '})

    // Click the button that schedules the dialog to appear after three seconds.
    // Before clicking, Playwright automatically waits for the button to be actionable:
    // attached to the DOM, visible, stable, enabled, and able to receive pointer events.
    await dialogWithDelayForm.getByRole('button', {name: '3 seconds'}).click()

    // Create a locator for the dialog container that will be added to the DOM later.
    // Creating a locator does not immediately search for the element or wait for it to appear.
    const dialogContainer = page.locator('nb-dialog-container')

    // This action is intentionally commented out so the example below can demonstrate
    // that not every locator method has the same auto-waiting behavior.
    // If enabled, click() would automatically wait for the delayed dialog and its "Ok"
    // button to become actionable before performing the click.
    // await dialogContainer.getByRole('button', {name: 'Ok'}).click()

    // This alternative is also intentionally commented out.
    // textContent() waits for a matching header element to be attached before reading it,
    // so it can handle the delayed appearance better than allTextContents() in this example.
    // const dialogHeader = await dialogContainer.locator('nb-card-header').textContent()

    // Read the text of every header that currently matches the locator.
    // allTextContents() returns immediately with the current matches and does not wait for
    // the delayed header to appear, so this can produce an empty array.
    const dialogHeader = await dialogContainer.locator('nb-card-header').allTextContents() 

    // Verify that the array contains the expected header text.
    // This generic assertion does not retry, so it fails when allTextContents() returned
    // before the dialog was rendered.
    expect(dialogHeader).toContain('Friendly reminder')
});

test('Alternative waits', async ({page}) => {

    // Locate the card used to open a dialog after a configured delay.
    const dialogWithDelayForm = page.locator('nb-card', { hasText: 'Open Dialog With Delay '})

    // Start the three-second timer that will eventually display the dialog.
    await dialogWithDelayForm.getByRole('button', {name: '3 seconds'}).click()

    // Define a reusable locator for the dialog that has not appeared yet.
    const dialogContainer = page.locator('nb-dialog-container')

    // OPTION 1: Wait explicitly for the element through its locator.
    // waitFor() waits for the locator to become visible by default. This is preferable
    // when the locator has already been defined and no assertion is needed yet.
    // await dialogContainer.waitFor()

    // waitForSelector() provides a similar explicit wait using a selector string.
    // Locator-based APIs are generally preferred because locators are reusable and
    // integrate naturally with Playwright's auto-waiting and strictness checks.
    // await page.waitForSelector('nb-dialog-container')

    // OPTION 2: Wait for the network response that causes or confirms the delayed result.
    // The glob pattern matches a response URL containing "/delay/" followed by any value.
    // In flows where the action triggers the request immediately, the response wait should
    // normally be registered before or at the same time as the action to avoid a race condition.
    // await page.waitForResponse('**/delay/*')

    // OPTION 3: Wait until there are no active network connections for a short period.
    // networkidle is discouraged for test synchronization because unrelated background
    // requests can make it slow or unreliable; waiting for a specific UI state is clearer.
    // await page.waitForLoadState('networkidle')

    // OPTION 4: Pause for a fixed amount of time.
    // Hardcoded waits are strongly discouraged: they waste time when the UI is fast and
    // still fail when the UI takes longer than expected. Prefer condition-based waits.
    // await page.waitForTimeout(3500)

    // This code is intentionally commented out because allTextContents() does not wait
    // for the delayed header. Without one of the explicit waits above, it may return an
    // empty array, and the following generic assertion would fail without retrying.
    // const dialogHeader = await dialogContainer.locator('nb-card-header').allTextContents()
    // expect(dialogHeader).toContain('Friendly reminder')

    // PREFERRED OPTION: Assert directly against the locator.
    // toHaveText() automatically retries until the header appears with the expected text
    // or the assertion timeout is reached, combining synchronization and verification.
    await expect(dialogContainer.locator('nb-card-header')).toHaveText('Friendly reminder')
});

test('Timeouts', async({page}) => {
    test.setTimeout(120000) // You can change the timeout for specific tests.
    test.slow() // Slow test will be given triple the default timeout
    const dialogWithDelayForm = page.locator('nb-card', { hasText: 'Open Dialog With Delay '})
    await dialogWithDelayForm.getByRole('button', {name: '3 seconds'}).click()
    const dialogContainer = page.locator('nb-dialog-container')

    // You can change the timeout for specific actions
    await dialogContainer.getByRole('button', {name: 'Ok'}).click({timeout: 4000})

});
