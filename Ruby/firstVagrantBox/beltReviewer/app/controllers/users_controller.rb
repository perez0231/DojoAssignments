class UsersController < ApplicationController
  def index
  end

  def create
    @user=User.create(fname: params[:fname], lname: params[:lname], email: params[:email], city: params[:city], state: params[:state], password: params[:password], password_confirmation: params[:password_confirmation])
    if @user.valid?
      session[:user_id]=@user.id
      redirect_to '/events/index'
    else
      flash[:errors] = @user.errors.full_messages
      redirect_to "/"
    end
  end

  def new
    @user= User.find_by(email:params[:email]).try(:authenticate, params[:password])
    if @user
      session[:user_id]=@user.id
      redirect_to '/events/index'
    else
      flash[:errors]=@user.errors.full_messages
      redirect_to "/"
  end
end
  def show
  end

  def edit
    @user= User.find(session[:user_id])
  end

  def update
  end

  def destroy
  end
  def logout
    session.clear
    redirect_to "/"
  end
end
