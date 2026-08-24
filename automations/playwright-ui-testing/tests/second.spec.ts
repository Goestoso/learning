import { expect, test } from '@playwright/test';

test.beforeEach(async ({ page }) => {
  await page.goto('https://playground.bondaracademy.com/');
  await page.getByText('Forms').click();
  await page.getByText('Form Layouts').click();
});

test('Locator Syntax Rules', async ({ page }) => {
  // find by Tag
  page.locator('input') // anything is just a tag for the playwright

  // find by ID
  page.locator('#inputEmail1') // if it has # it means that it is looking for an ID

  // find by Class
  page.locator('.shape-rectangle') // if it has . it means that it is looking for a class

  // find by any attribute
  page.locator('[placeholder="Email"]') // if it has [] it means that it is looking for an attribute

  // find by full class value
  page.locator('[class="input-full-width size-medium status-basic shape-rectangle nb-transition"]') // if it has [] it means that it is looking for an attribute

  //find by multiple attributes
  page.locator('input[placeholder="Email"].shape-rectangle') // its looking for an input tag with placeholder attribute and class attribute

  //find by xpath (NOT RECOMMENDED)
  page.locator('//*[@id="inputEmail1"]') // if it has // it means that it is looking for an xpath // * means that it is looking for any tag with the attribute id="inputEmail1"

  // find by partial text match
  page.locator(':text("Using")') // if it has :text() it means that it is looking for a text match

  // find by exact text match
  page.locator(':text-is("Using the Grid")') // if it has :text-is() it means that it is looking for a exact text match
});

test('User-visible locators', async ({ page }) => {
  // Find an element by its ARIA (Accessible Rich Internet Applications) role and accessible name.
  // ARIA explains the meaning, name, and state of page elements to those who cannot interpret the interface solely through visual means.
  // Here, it finds the first button named "Submit".
  await page
    .getByRole('button', { name: 'Submit' })
    .first()
    .click();

  // Find a text input by its ARIA role and accessible name.
  await page
    .getByRole('textbox', { name: 'Email' })
    .first()
    .fill('test@test.com');

  // Find a form control by the text of its associated label.
  await page
    .getByLabel('Email')
    .first()
    .fill('test@test.com');

  // Find an input by its placeholder text.
  await page
    .getByPlaceholder('Jane Doe')
    .fill('Artem Bondar');

  // Find an element by its visible text content.
  await page
    .getByText('Submit')
    .first()
    .click();

  // Find an element by its data-testid attribute.
  // Test IDs provide an explicit and stable contract for automated tests.
  await page
    .getByTestId('inputEmail1')
    .fill('test@test.com');

  // Find an element by the value of its title attribute.
  await page
    .getByTitle('IoT Dashboard')
    .click();
});

test('Locating child elements', async ({ page }) => {
  // Locate "Option 1" by chaining locators from the card to its nested radio group, then click it.
  await page.locator('nb-card').locator('nb-radio-group').locator(':text-is("Option 1")').click()

  // Locate "Option 2" with a single descendant CSS selector and click it.
  await page.locator('nb-card nb-radio-group :text-is("Option 2")').click()

  // Find the first "Sign in" button inside any card by its accessible role and name, then click it.
  await page.locator('nb-card').getByRole('button', { name: 'Sign in' }).first().click();

  // Select the fourth card by its zero-based index, find its button, and click it.
  // Using an index is possible, but it is not recommended because changes to the page order can make the test fragile.
  await page.locator('nb-card').nth(3).getByRole('button').click()
});

test('Locating parent elements', async ({page}) => {
  // Locate the parent <nb-card> whose text content includes "Using the Grid".
  // The hasText option filters the cards before Playwright searches inside the matching card.
  // Then, find the button within that card by its accessible role and click it.
  await page.locator('nb-card', {hasText: 'Using the Grid'}).getByRole('button').click()

  // Locate the parent <nb-card> that contains the element with the ID "inputEmail1".
  // The has option accepts another locator and keeps only parents containing a matching descendant.
  // After identifying the correct card, find its button by role and click it.
  await page.locator('nb-card', {has: page.locator('#inputEmail1')}).getByRole('button').click()

  // Start by locating all <nb-card> elements on the page.
  // Use filter() with hasText to keep only the card containing the text "Using the Grid".
  // Finally, locate the button inside the filtered card and click it.
  await page.locator('nb-card').filter({hasText: 'Using the Grid'}).getByRole('button').click()

  // Create a locator representing every <nb-card> element on the page.
  await page.locator('nb-card')
  // Keep only cards that contain an <nb-checkbox> descendant.
  .filter({has: page.locator('nb-checkbox')})
  // Narrow the result further to the card whose text also includes "Sign in".
  .filter({hasText: 'Sign in'})
  // Inside the remaining card, locate the form control associated with the "Email" label.
  .getByLabel('Email')
  // Fill the selected email field with the provided test value.
  .fill('test@test.com')

  // Locate the element containing the visible text "Using the Grid.".
  // The ".." selector moves one level up the DOM tree to that element's direct parent.
  // From the parent, find a descendant button by its accessible role and click it.
  // This parent traversal works, but filtering a stable parent locator is usually clearer and less fragile.
  await page.getByText('Using the Grid.').locator('..').getByRole('button').click()
});

test('Reusing locators', async ({page}) => {
  const basicFormSection = page.locator('nb-card', {hasText: 'Basic form'})
  const emailInputField = basicFormSection.getByLabel('Email')

  await emailInputField.fill('test@test.com')
  await basicFormSection.getByLabel('Password').fill('playwright')
  await basicFormSection.locator('nb-checkbox').click()
  await basicFormSection.getByRole('button').click()

  await expect(emailInputField).toHaveValue('test@test.com')
});