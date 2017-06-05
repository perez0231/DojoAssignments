require 'test_helper'

class NinjaGoldControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get ninja_gold_index_url
    assert_response :success
  end

  test "should get new" do
    get ninja_gold_new_url
    assert_response :success
  end

end
