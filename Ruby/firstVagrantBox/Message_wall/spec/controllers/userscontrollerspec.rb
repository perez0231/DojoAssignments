require 'rails_helper'
describe UsersController, type: :controller do
  it "routes /users to the users controller" do
    expect(:get => "/").to route_to(:controller => "users", :action => "index")
  end
 it "routes /message/ to users message" do
   expect(:get => "/messages/").to route_to(:controller => "messages", :action => "index")
 end
 it "routes /comment/:id to message page" do
   expect(:post => "/comment/1").to route_to(:controller => "messages", :action => "create_comment", :id => "1")
 end
end
