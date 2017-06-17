import { GithubScoreAppPage } from './app.po';

describe('github-score-app App', () => {
  let page: GithubScoreAppPage;

  beforeEach(() => {
    page = new GithubScoreAppPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
