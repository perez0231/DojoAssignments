import { RegistrationAppPage } from './app.po';

describe('registration-app App', () => {
  let page: RegistrationAppPage;

  beforeEach(() => {
    page = new RegistrationAppPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
