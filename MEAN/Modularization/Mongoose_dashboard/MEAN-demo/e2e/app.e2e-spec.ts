import { MEANDemoPage } from './app.po';

describe('mean-demo App', () => {
  let page: MEANDemoPage;

  beforeEach(() => {
    page = new MEANDemoPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
