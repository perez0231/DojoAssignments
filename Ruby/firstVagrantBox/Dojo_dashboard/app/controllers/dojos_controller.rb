class DojosController < ApplicationController
  def index
    @dojos=Dojo.all

  end

  def new
  end

  def show
  @dojo=Dojo.find(params[:id])
  end

  def destroy
    Dojo.find(params[:id]).delete
    redirect_to "/"
  end

  def update
    Dojo.find(params[:id]).update(branch: params[:branch], street:params[:street], city:params[:city], state: params[:state])
  redirect_to '/'
  end

  def create

    #Dojo.create(branch: params[:branch], street:params[:street], city:params[:city], state: params[:state])
    @dojo= Dojo.new(dojo_params)

    if @dojo.save
      redorect to root_url, notice: "created a dojo"
    else
      flash[:errors] = @dojo.errors.full_messages
      redirect_to :back
    redirect_to '/'
  end
  end

  def edit
    @dojo=Dojo.find(params[:id])
  end


  private
    def dojo_params
      params.require(:dojo).permit(:branch, :street, :city, :state)
    end
end
