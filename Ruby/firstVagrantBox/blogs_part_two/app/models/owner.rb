class Owner < ApplicationRecord::Base
  belongs_to :user
  belongs_to :blog
end


#creating a many-to-many between user and blog
