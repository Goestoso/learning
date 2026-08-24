import { test} from '@playwright/test';

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