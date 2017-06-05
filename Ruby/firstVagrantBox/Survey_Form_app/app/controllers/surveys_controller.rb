class SurveysController < ApplicationController
  def index
    session[:views] ||=0
  end
  def create
    #adds the value in params[:id] to the :id key in session


    session[:views]= session[:views] +1

    session[:result]= params[:survey]
    flash[:count] = "You have submitted this form #{ session[:views] } times"
    redirect_to '/new'
  end

  def new
    @result= session[:result]

  end
end
