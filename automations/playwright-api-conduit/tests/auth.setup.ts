import { test as setup, expect } from '@playwright/test';
import path from 'path';
import fs from 'fs';

const authFile = path.join(__dirname, '../playwright/.auth/user.json');

setup('authenticate', async ({ page, request }) => {
  if (fs.existsSync(authFile)) { //updating the storage file if it already exists, because we can save time by not logging in via the UI
    const loginResponse = await request.post('https://conduit-api.bondaracademy.com/api/users/login', { //post to get the session token
      data: {
        "user": {
          "email": "tbshield@test.com",
          "password": "tbshield@123"
        }
      }
    }); 
    expect(loginResponse.status()).toEqual(200) //always good to verify if the api request worked
    const responseLoginJSON = await loginResponse.json()
    const token = responseLoginJSON.user.token

    const storageStateFile = JSON.parse(fs.readFileSync(authFile, 'utf8')) 
    storageStateFile.origins[0].localStorage[0].value = token
    fs.writeFileSync(authFile, JSON.stringify(storageStateFile, null, 2)) 
  } else {
    // Perform authentication steps via the UI
    await page.goto('https://conduit.bondaracademy.com')
    await page.getByText('Sign in').click()
    await page.getByPlaceholder('Email').fill('tbshield@test.com')
    await page.getByPlaceholder('Password').fill('tbshield@123')
    await page.getByRole('button', { name: 'Sign in' }).click()
    // Wait until the page receives the cookies.
    //
    // Sometimes login flow sets cookies in the process of several redirects.
    // Wait for the final URL to ensure that the cookies are actually set.
    //await page.waitForURL('https://github.com/');
    // Alternatively, you can wait until the page reaches a state where all cookies are set.
    await expect(page.getByRole('link', { name: 'New Article' })).toBeVisible();

    // End of authentication steps.

    await page.context().storageState({ path: authFile });

  }
});