require 'rails_helper'
feature "User makes a message" do
  before(:each) do
    visit '/'
    fill_in 'username', with: "users_username"
    click_button 'login'
  end
  scenario 'succesfuly create a new message' do
    fill_in "content", with: "this is a new message mang"
    click_button "Submit!"
    expect(page).to have_content "this is a new message mang"
    expect(current_path).to eq('/messages')
  end
  scenario 'message field is blank' do
    click_button "Submit!"
    expect(page).to have_content "Content can't be blank"
    expect(current_path).to eq('/messages')
  end
  scenario 'user should logout' do
    click_link('Logout!')
    expect(current_path).to eq('/')
  end
  end
