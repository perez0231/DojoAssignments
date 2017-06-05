Rails.application.routes.draw do
  root 'surveys#index'

  post '/create' => 'surveys#create'
  get '/new' =>'surveys#new'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
