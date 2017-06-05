class User < ApplicationRecord
  has_secure_password
  EMAIL_REGEX = /\A[\w+\-.]+@[a-z\d\-]+(\.[a-z\d\-]+)*\.[a-z]+\z/i
  validates :name, :email, :password, :password_confirmation, presence: true
  validates :email, uniqueness: {case_sesitive: false}, format: {with: EMAIL_REGEX}
  validates :password, :password_confirmation, length: {minimum: 7}
  before_save :email_downcase

  def email_downcase
  self.email.downcase
  end

end
