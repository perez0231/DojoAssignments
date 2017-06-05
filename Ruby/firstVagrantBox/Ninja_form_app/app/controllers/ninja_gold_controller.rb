class NinjaGoldController < ApplicationController
  def index
    session[:count] ||= 0
    session[:activities] ||= []
    @activities =session[:activities]
    @gold =session[:count]
  end

  def create
    if params['building'] == 'farm'
      gold = rand(10..20)
    elsif params['building'] == 'cave'
      gold = rand(5..10)
    elsif params['building'] == 'house'
      gold = rand(2..5)
    elsif params['building'] == 'casino'
      gold = rand(-50..50)
    end

    curr_time =Time.now

    if gold > 0
      session[:activities] << "Earned #{gold} gold from the #{params[:building]}! @ (#{curr_time.strftime('%Y/%m/%d %l:%M %P')})"
    else
      session[:activities] << "Entered a casino and lost #{gold} golds... Ouch. (#{curr_time.strftime('%Y/%m/%d %l:%M %P')})"
    end
    session[:count] += gold
    redirect_to :root
  end
end
