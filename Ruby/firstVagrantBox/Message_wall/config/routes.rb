Rails.application.routes.draw do
  root 'users#index'

  post 'login' => 'users#login'

  get 'users' => 'users#new'

  get 'users/logout' => 'users#logout'

  get 'messages/' => 'messages#index'

  post '/messages' => 'messages#create'

  post 'comment/:id' => 'messages#create_comment'



  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
