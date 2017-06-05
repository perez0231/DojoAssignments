class User < ApplicationRecord
EMAIL_REGEX = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i
has_many :owners
has_many :messages
has_many :posts

has_many :comments, as: :commentable

#blogs owned by user
has_many :blogs, through: :owners

#all blogs user posted on
has_many :blogs, through: :owners
#all blogs user has posted
has_many :blog_posts, through: :posts, source: :blog
validates :email, uniqueness: { case_sensitive: false }, format: { with: EMAIL_REGEX }
validates :fname, :lname, :email, presence: true
end
