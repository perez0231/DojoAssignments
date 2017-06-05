class Event < ApplicationRecord
  validates :name, :date, :city, :state, :user, presence: true

  belongs_to :user
  has_many :comments
  has_many :users_attending, through: :participants, source: :user
  has_many :users_comments, through: :comments, source: :user
end
