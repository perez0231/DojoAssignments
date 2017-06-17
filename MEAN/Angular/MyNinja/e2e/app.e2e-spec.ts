import { MyNinjaPage } from './app.po';

describe('my-ninja App', () => {
  let page: MyNinjaPage;

  beforeEach(() => {
    page = new MyNinjaPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
