import { test } from '@playwright/test';

//function step is a decorator that wraps the original method and adds a test.step around it. 
// It takes two parameters: target and context. The target parameter is the original method that we want to decorate, 
// and the context parameter provides information about the method being decorated, such as its name and the class it belongs to.
export function step(target: Function, context: ClassMethodDecoratorContext) {
  return function replacementMethod(this: any, ...args: any) {
    const name = this.constructor.name + '.' + (context.name as string);
    return test.step(name, async () => {
      return await target.call(this, ...args);
    },);
  };
}
