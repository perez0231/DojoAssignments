Rails.application.routes.draw do


  root 'dojos#index'
  get 'dojos/new'=> "dojos#new"
  get "dojos/:id" => "dojos#show"
  delete 'dojos/:id' => 'dojos#destroy'
  get 'dojos/:id/edit' => 'dojos#edit'
  patch 'dojos/:id' => 'dojos#update'
  post 'dojos/create' => 'dojos#create'

  get '/dojos/:dojo_id/students' => 'students#index'
  get '/dojos/:dojo_id/students/new' => 'students#new'
  post '/dojos/:dojo_id/students' => 'students#create'
  get '/dojos/:dojo_id/students/:id' => 'students#show'
  get '/dojos/:dojo_id/students/:id/edit' => 'students#edit'
  patch '/dojos/:dojo_id/students/:id' => 'students#update'
  delete '/dojos/:dojo_id/students/:id' => 'students#edit'


  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
