class User < ApplicationRecord
  has_secure_password
  EMAIL_REGEX = /\A[\w+\-.]+@[a-z\d\-]+(\.[a-z\d\-]+)*\.[a-z]+\z/i
  validates :name, :email, :password, :password_confirmation, presence: true

  has_many :users_likes, through: :likes, source: :user
  validates :email, uniqueness: {case_sesitive: false}, format: {with: EMAIL_REGEX}
  before_save :email_downcase

  def email_downcase
    self.email.downcase
  end



  has_many :secrets
  has_many :likes, dependent: :destroy
  has_many :secrets_liked, through: :like, source: :secret
end
