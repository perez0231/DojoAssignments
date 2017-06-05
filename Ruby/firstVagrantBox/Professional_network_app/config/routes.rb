Rails.application.routes.draw do
  get 'networks/new'

  get 'networks/:id' => "networks#create"

  get 'invitations/index'

  post 'invitations/:id/create' => "invitations#create"

  delete 'invitations/:id/' => "invitations#destroy"

  root "user#index"

  post 'user/new' => "user#new"

  post 'user/' => "user#create"

  get 'user/all' => "user#all"

  get 'user/network' => "user#network"

  delete 'users/logout' => "user#logout"

  get 'user/:id/edit'=> "user#edit"

  get 'user/:id/show'=> "user#show"

  patch 'user/:id' => "user#update"






  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
