Rails.application.routes.draw do
  get 'events/index' => "events#index"

  post 'events' => "events#create"

  get 'events/new'

  get 'events/:id'=> "events#show"

  get 'events/:id/edit'=> "events#edit"

  patch 'events/:id' => "events#update"

  post "events/:id/comments" => "events#comments"

  get "events/:id/delete" => "events#destroy"

  get "events/:id/cancel" => "events#cancel"

  get "events/:id/join"=> "events#join"

  root "users#index"

  post 'users' => "users#create"

  post 'users/new'

  get 'users/show'

  get 'users/:id/edit' => "users#edit"

  get 'users/:id' => "users#update"

  get 'users/destroy'

  delete 'users/logout'=> 'users#logout'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
