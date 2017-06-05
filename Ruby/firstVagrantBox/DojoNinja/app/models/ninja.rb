class Ninja < ApplicationRecord
  belongs_to :dojo
  validates :fname, :lname, presence:true
end
