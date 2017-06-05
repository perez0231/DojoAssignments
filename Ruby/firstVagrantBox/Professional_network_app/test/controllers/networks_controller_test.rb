require 'test_helper'

class NetworksControllerTest < ActionDispatch::IntegrationTest
  test "should get new" do
    get networks_new_url
    assert_response :success
  end

  test "should get create" do
    get networks_create_url
    assert_response :success
  end

  test "should get destroy" do
    get networks_destroy_url
    assert_response :success
  end

end
