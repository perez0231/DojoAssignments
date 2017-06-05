require 'rails_helper'
feature "User creates an account" do
  before(:each) do
    visit '/'
  end
  scenario 'User created succesfully' do
    fill_in "username", with: "jimmyMixer"
    click_button "login"
    expect(page).to have_content "Hello jimmyMixer"
    expect(current_path).to eq('/messages')
  end
  scenario "User creation not succesful" do
    click_button "login"
    expect(page).to have_content "Username can't be blank"
    expect(page).to have_content "Username is too short (minimum is 6 characters)"
    expect(current_path).to eq('/')

  end

end
