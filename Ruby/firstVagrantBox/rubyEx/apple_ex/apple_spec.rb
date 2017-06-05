require_relative 'apple_tree' # include our Project class in our spec file


RSpec.describe Apple_tree do
  before (:each) do
  @daniel =Apple_tree.new(4)
  end

it 'should have an age attribute with getter and setter' do
  @daniel.age = 100
  expect(@daniel.age= 100)
end
  it 'should have a getter for height' do
    expect(@daniel.height).to eq(10)
    expect{@daniel.height=2}.to raise_error(NoMethodError)
  end
  it 'should raise NoMethodError when setting the height' do
    expect{@daniel.apple_count=2}.to raise_error(NoMethodError)
  end


context "should have a method year_gone_by" do
  before(:each) do
      @daniel.year_gone_by
    end

    it 'adds a year to the age attribute' do
      expect(@daniel.age).to eq(5)
    end
    it 'add ten per cent to the height attribute' do
      expect(@daniel.height).to eq(11)
    end
    it 'add 2 apples to the apple_count' do
      expect(@daniel.apple_count).to eq(2)
    end
end

it 'should only grow apples between 4 and 10' do
  7.times{@daniel.year_gone_by}
  expect(@daniel.apple_count).to eq(12)
end

it 'all the apples should be all the apples' do
  @daniel.pick_apples
  expect(@daniel.apple_count).to eq(0)
end




end
