import { QuoteApplicationPage } from './app.po';

describe('quote-application App', () => {
  let page: QuoteApplicationPage;

  beforeEach(() => {
    page = new QuoteApplicationPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
