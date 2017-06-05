Rails.application.routes.draw do
  root "user#index"

  post 'user/new' => "user#new"

  post 'user/' => "user#create"

  get 'user/edit'

  get 'user/delete'

  get 'user/:id'=> "user#show"

  get 'user/update'

  get 'user/network' => "user#network"

  get 'user/all' => "user#all"

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
