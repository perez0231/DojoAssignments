class Message < ApplicationRecord::Base
  belongs_to :user
  belongs_to :blog
  validates :author, :message, presence:true
end
