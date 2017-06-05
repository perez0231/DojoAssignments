class Bank_Account
  attr_reader :checking_balance, :savings_balance, :account_number
  @@bank_accounts=0 #global class variable

  def self.bank_total_accounts
    puts @@bank_accounts
  end




  def initialize(savings, checkings)
    puts "new account created"
    @account_number = account_number_generator
    @checking_balance=checkings
    @savings_balance=savings
    @interest_rate= 0.01
    @@bank_accounts += 1

  end

  def show_all_balances
    p "Checkings :#{@checking_balance} "
    p "Savings :#{@savings_balance} "
    p "Total :#{@checking_balance + @savings_balance}"
  end
  def check_checkings
    "Checkings: #{@checking_balance}"
  end

  def total_accounts
    "Total: #{@checking_balance + @savings_balance}"
  end

  def account_info
    puts "Account Number is: #{@account_number}"
    puts "Interest Rate: #{@interest_rate}"
    show_all_balances
  end

  def deposit(account, amount)
    if account.downcase == "checkings"
        @checking_balance += amount
        puts "Deposited Cash into your Checkings account"
    elsif account.downcase =="savings"
      @savings_balance += amount
      puts "depostited cash into your savings account"

    else
      puts "must put savings or checkings please"
  end
end






  def withdraw(account, amount)
    if account.downcase == "checkings"
      if amount > @checking_balance
        puts "insufficent funds"
      else
        @checking_balance -=amount
      end
    elsif account.downcase == "savings"
      if amount > @savings_balance
        puts "insufficent funds"
      else
        @savings_balance -=amount
      end
    else
      puts "wrong account info"
    end
  end

  private
    def account_number_generator
      rand(10000..999999)
    end

end
dorian=Bank_Account.new(1, 50)
daniel=Bank_Account.new(10, 1000)
daniel.show_all_balances
daniel.account_info
daniel.deposit("checkings", 10)
daniel.withdraw("savings", 10)
daniel.show_all_balances
Bank_Account.bank_total_accounts
