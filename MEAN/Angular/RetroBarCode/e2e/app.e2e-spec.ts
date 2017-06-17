import { RetroBarCodePage } from './app.po';

describe('retro-bar-code App', () => {
  let page: RetroBarCodePage;

  beforeEach(() => {
    page = new RetroBarCodePage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
