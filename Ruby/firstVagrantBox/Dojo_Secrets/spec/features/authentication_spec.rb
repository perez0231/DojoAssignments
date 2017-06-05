require 'rails_helper'
feature 'authentication feature' do
  before(:each) do
    @user= create(:user)
  end
  feature "user attempts to sign in" do
    scenario 'visits sign in page, promoted with email and pass field' do
      visit '/'
      expect(page).to have_field("email")
      expect(page).to have_field("password")
    end
    scenario 'logs in user if email and password valid' do
      log_in
      expect(current_path).to eq("/secrets")
      expect(page).to have_text(@user.name)
    end

    scenario 'does not sign in user if email not found' do
      log_in email: 'wrong email'
      expect(current_path).to eq("/")
      expect(page).to have_text("Invalid Combination")
    end
    scenario 'does not sign in user if email pass combo is invalid'

  end

  feature "user attempts to log out" do
    scenario 'display "Log Out" button when user is logged on'
    scenario 'logs out user and redirectss to login '
  end
end
