Rails.application.routes.draw do
  get 'secrets/index'

  root 'users#new'

  post 'sessions/create' => 'sessions#create'

  post 'sessions/new' => 'sessions#new'

  delete 'sessions/:id' => 'sessions#delete'

  get 'users/index'

  get 'users/:id' => "users#index"

  get 'users/register'

  get 'users/logout'

  get 'users/show'

  get 'users/:id/edit' => 'users#edit'

  get 'secrets/'=>  'secrets#index'

  post 'secrets/create' => 'secrets#create'

  post 'secrets/likes/:id'=> 'secrets#like'

  delete 'secrets/likes/:id'=> 'secrets#unlike'

  patch 'secrets/:id'=> 'secrets#update'

  delete 'secrets/:id' => 'secrets#delete'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
