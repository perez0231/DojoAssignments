require_relative 'bank' # include our Project class in our spec file


RSpec.describe Bank_Account do
  before (:each) do
    @daniel =Bank_Account.new(10000, 10000)
  end
  it 'has a getter for retrieving checkings info' do
    expect(@daniel.check_checkings).to eq("Checkings: 10000")
  end

  it 'has a getter for retrieving total value info' do
    expect(@daniel.total_accounts).to eq("Total: 20000")
  end
  it 'has a withdraw function' do
    @daniel.withdraw("checkings", 10)
    expect(@daniel.check_checkings).to eq("Checkings: 9990")
  end

  it 'raises error if user withdraws too much cash' do
  expect{@daniel.withdraw("checkings", 10001)}.to output("insufficent funds\n").to_stdout
end

it 'raises eerror if total num of bank accounts queried' do
  expect{@daniel.bank_total_accounts}.to raise_error(NoMethodError)
end

it 'user attempts to change interest_rate error' do
  expect{@daniel.interest_rate}.to raise_error(NoMethodError)
end



end
