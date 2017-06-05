class User < ApplicationRecord
has_secure_password
EMAIL_REGEX = /\A[\w+\-.]+@[a-z\d\-]+(\.[a-z\d\-]+)*\.[a-z]+\z/i
validates :fname, :lname, :email, :city, :state, :password, :password_confirmation, presence: true


validates :email, uniqueness: {case_sesitive: false}, format: {with: EMAIL_REGEX}
validates :password, :password_confirmation, length: {minimum: 8}
before_save :email_downcase


has_many :events
has_many :comments, dependent: :destroy
has_many :participants
has_many :attending, through: :participants, source: :event
has_many :events_commented, through: :comments, source: :events

def email_downcase
  self.email.downcase
end
end
