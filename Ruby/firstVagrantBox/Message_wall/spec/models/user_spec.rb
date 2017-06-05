require 'rails_helper'
RSpec.describe User, type: :model do
  context "With valid attributes" do
    it "should save" do
      user = User.create(
      username: "harrypotter"
      )
      expect(user).to be_valid
    end
  end
  context "with invalid attributes" do
    it "should be unique" do
      user1 =User.create(
      username: "harrypotter"
      )
      user2 =User.create(
      username: "harrypotter"
      )
      expect(user2).to be_invalid
    end
    it "should be longer than 5" do
      user1 =User.create(
      username: "jim"
      )

      expect(user1).to be_invalid
    end
    it "should be longer than 5" do
      user1 =User.create(
      username: ""
      )

      expect(user1).to be_invalid
    end

end
end
