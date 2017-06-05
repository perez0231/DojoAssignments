class User < ApplicationRecord
  validates :first_name, :last_name, :email, :password, :age, presence: true
  validates :age, numericality: {greater_than:10, less_than:150}
  validates :first_name, :last_name, length: {in: 2..30}


  def messages
    User.find_by_sql("SELECT * FROM messages WHERE messages.user_id = #{self.id}")
  end
end
