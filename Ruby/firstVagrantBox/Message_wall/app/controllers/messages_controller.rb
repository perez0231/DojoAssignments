class MessagesController < ApplicationController
  def index
    @user= User.find(session[:user_id])
    @messages= Message.all
    @comments=Comment.all
  end

  def create
    user=User.find(session[:user_id])
    @message=Message.create(content: params[:content], user: user)
    if @message.valid?
      redirect_to '/messages'
    else
      flash[:errors]=@message.errors.full_messages
      redirect_to '/messages'
    end
  end

  def create_comment
    user=User.find(session[:user_id])
    message=Message.find(params[:id])
    @comment= Comment.create(content: params[:content], user: user, message: message)
    if @comment.valid?
      redirect_to '/messages'
    else
      flash[:errors]=@comment.errors.full_messages
      redirect_to '/messages'
    end

  end
end
