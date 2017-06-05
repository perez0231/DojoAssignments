class UserController < ApplicationController
  def index
  end

  def new
    @users= User.find_by(email:params[:email]).try(:authenticate, params[:password])
  if @users
    session[:user_id]=@users.id
    redirect_to '/user/network'
  else
    flash[:errors] = @users.errors.full_messages
    redirect_to "/"
  end

  end

  def create
    @user=User.create(name: params[:name], email: params[:email], password: params[:password], password_confirmation: params[:password_confirmation], description: params[:description])
  if @user.valid?
    session[:user_id]=@user.id
    redirect_to '/user/network'
  else
    flash[:errors] = @user.errors.full_messages
    redirect_to "/"
  end
  end

  def edit
  end

  def delete
  end

  def show
    @user= User.find(params[:user_id])
  end
  def network
    @user=User.find(session[:user_id])
  end

  def update
  end

  def all
    @user=User.all
  end
end
