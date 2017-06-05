class SessionsController < ApplicationController
  before_action :required_login, except: [:new, :create]
  def new
    @user = User.find_by(email: params[:email]).try(:authenticate, params[:password])
    if @user
      session[:user_id]=@user.id
    redirect_to "/secrets"
    else
    flash[:errors] = @user.errors.full_messages
    redirect_to "/"
  end
  end


  def create
    @user=User.create(name: params['name'], email: params['email'], password: params['password'], password_confirmation: params['password_confirmation'])
    if @user.valid?
      session[:user_id]=@user.id
      redirect_to '/secrets'
    else
      flash[:errors] = @user.errors.full_messages
      redirect_to "/"
    end

  end

  def delete
    session.clear
    redirect_to "/"
  end
end
