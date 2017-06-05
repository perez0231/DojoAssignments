class UsersController < ApplicationController
  before_action :required_login, except: [:new, :login, :register]
  #before action :require_Correct_user, only [profile edit update destroy]
  def index
    @user=User.find(session['user_id'])
    @secrets=Secret.where(user: session['user_id'])
    @secret=Secret.all
  end

  def login
  end

  def register
  end

  def new
  end

  def logout
  end

  def update
    User.find(params[:user_id]).update(name: params[:name], email:params[:email], password:params[:password], password_confirmation: params[:password_confirmation])
  end

  def edit
    @user = User.find(session[:user_id])
  end
end
