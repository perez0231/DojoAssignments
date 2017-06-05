require 'rails_helper'

RSpec.describe User, type: :model do
  context "With valid attributes" do
    it "should not have first name blank" do
      user=User.new(
        first_name:'' ,
        last_name: 'chang',
        email: "email@me.com"
      )
    expect(user).to be_invalid
  end
end


context "with invalid attributes" do
  it "should not save if first_name is blank" do
    user=User.new(
      first_name:'' ,
      last_name: 'chang',
      email: "email@me.com"
    )
    expect(user).to be_invalid
  end
  it "should not save if last name blank" do
    user=User.new(
    first_name:"dan",
    last_name: "",
    email: 'dp@gmail'
    )
    expect(user).to be_invalid
  end

  it "should not save if email already exists" do
    user=User.new(
    first_name:"dan",
    last_name: "",
    email: 'dp@gmail'
    )
    expect(user).to be_invalid
end
    it "should contain a valid email" do
    user = User.new(
     first_name: 'Roald',
     last_name: 'Dahl',
     email: 'roalddahl'
    )
    expect(user).to be_valid
  end
  end
end
