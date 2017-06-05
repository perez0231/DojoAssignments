Rails.application.routes.draw do
  root 'ninja_gold#index'
  post '/create' => 'ninja_gold#create'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
