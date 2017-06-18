import { DojoWeatherAppPage } from './app.po';

describe('dojo-weather-app App', () => {
  let page: DojoWeatherAppPage;

  beforeEach(() => {
    page = new DojoWeatherAppPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
