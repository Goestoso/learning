import { test as base } from '@playwright/test';
import { PageManager } from './page-objects/page-manager';

type FixtureTypes ={
    pom: PageManager
}

//Fixtures are executed regardless of whether the tests passes or fails

export const test = base.extend<FixtureTypes>({ //you can create yout custom fixtures
    pom: async({page}, use) => {
        await page.goto('/')
        const manager = new PageManager(page)

        //every code before this statement will be executed before the test, behave like a before hook or setup
        await use(manager) //the manager object will be available inside the tests 
        //every code after this statement will be executed after the test is completed, as a teardown step

    }
});
