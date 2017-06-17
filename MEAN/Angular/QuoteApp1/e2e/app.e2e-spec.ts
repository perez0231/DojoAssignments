import { QuoteApp1Page } from './app.po';

describe('quote-app1 App', () => {
  let page: QuoteApp1Page;

  beforeEach(() => {
    page = new QuoteApp1Page();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
