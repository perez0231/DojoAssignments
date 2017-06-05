class EventsController < ApplicationController
  def index
    @user= User.find(session[:user_id])
    @events= Event.all
    @count=Event.where(state: current_user.state).count
    except
    puts @count
  end

  def create
    user=User.find(session[:user_id])
    @event=Event.create(name: params[:name], date: params[:date], city: params[:city], state: params[:state], user: user)
    flash[:errors]= @event.errors.full_messages
    redirect_to '/events/index'
  end

  def new
  end

  def show
    @Event= Event.find(params[:id])
    @participants= Participant.where(event_id: params[:id])
    @comments= Comment.where(event_id: params[:id])

  end

  def cancel
    Participant.find_by(event: params[:id]).destroy
    redirect_to :back
  end

  def edit
    @Event= Event.find(params[:id])
  end

  def join
    event= Event.find(params[:id])
    user= User.find(session[:user_id])
    Participant.create(event: event, user: user)
    redirect_to :back

  end

  def update
    user=User.find(session[:user_id])
    Event.find(params[:id]).update(name: params[:name], date: params[:date], city: params[:city], state: params[:state], user: user)
    redirect_to '/events/index'
  end

  def destroy
    Event.find(params[:id]).destroy
    redirect_to "/events/index"
  end

  def comments
    user=User.find(session[:user_id])
    event= Event.find(params[:id])
    comment= Comment.create(content: params[:content], user: user, event: event)
    if comment.valid?
      redirect_to :back
    else
      flash[:errors]=comment.errors.full_messages
      redirect_to :back
    end

  end
end
