import { test, expect } from '@playwright/test';
import tags from '../test-data/tags.json'; //separate the test data from the test code, and import it as a JSON object. This makes it easier to manage and update the test data, and also allows for reusability across multiple tests.

test.beforeEach(async ({ page }) => {
  await page.route('*/**/api/tags', async route => { //* matches any URL that ends with /api/tags, regardless of the domain or path before it.

    await route.fulfill({ json: tags }); //Use json o send the response as JSON, and body to send the response body as a string. In this case, we are sending the tags object as a JSON response.
  });

  await page.route('*/**/api/articles*', async route => {
    const response = await route.fetch()
    const responseJSON = await response.json()
    responseJSON.articles[0].title = 'This is a mocked article title'
    responseJSON.articles[0].description = 'This is a mocked article description'
    await route.fulfill({ json: responseJSON });
  });

  await page.goto('https://conduit.bondaracademy.com');
});

test('Mocking API', async ({ page }) => { // useful for testing the UI without relying on the backend, or for testing how the UI behaves with different API responses. 
  await expect(page.locator('.navbar-brand')).toHaveText(/conduit/)
  await expect(page.locator('.sidebar .tag-pill')).toContainText(['Automation', 'Playwright'])
  await expect(page.locator('.preview-link h1').first()).toContainText('This is a mocked article title')
  await expect(page.locator('.preview-link p').first()).toContainText('This is a mocked article description')
});

