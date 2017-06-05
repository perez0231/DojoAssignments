class UsersController < ApplicationController

  def index
  end
  def login
    @user=User.find_by(username: params[:username])
    if @user
      session[:user_id]=@user.id
      redirect_to messages_path
    else
      @user=User.create(username: params[:username])
      if @user.valid?
        session[:user_id]=@user.id
        redirect_to messages_path
      else
        flash[:errors] = @user.errors.full_messages
        redirect_to "/"

      end
  end
end

  def new
  end

  def logout
    reset_session
    redirect_to "/"
  end


end
