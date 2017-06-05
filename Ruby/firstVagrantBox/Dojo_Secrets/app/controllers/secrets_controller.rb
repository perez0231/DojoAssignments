class SecretsController < ApplicationController
  before_action :required_login
  def index
    @secrets=Secret.all
    @user= User.find(session['user_id'])


  end

  def create
    user=User.find(session[:user_id])
    @secret=Secret.create(content: params[:content], user: user)
    flash[:errors]= @secret.errors.full_messages
    redirect_to "/secrets"

  end

  def delete
    Secret.find(params[:id]).destroy
    redirect_to "/secrets"
  end

  def like

    secret=Secret.find(params[:id])
    user=User.find(session[:user_id])
    Like.create(secret: secret, user: user)

    redirect_to "/secrets"
  end
  def unlike
    @like=Like.find(params[:id])
    @like.destroy if current_user=@like.user
    redirect_to "/secrets"
  end
end
