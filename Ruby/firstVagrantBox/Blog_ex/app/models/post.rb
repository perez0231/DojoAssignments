class Post < ApplicationRecord
  has_many :messages
  has_many :comments, as: :commentable


  belongs_to :user
  belongs_to :blog
  validates :content, :title, presence: true

end
