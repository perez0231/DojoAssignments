class UserController < ApplicationController
  def index
  end

  def edit
    @user= User.find(params[:id])
    puts @user
    puts "***"* 200
  end

  def new
    @user= User.find_by(email:params[:email]).try(:authenticate, params[:password])
    if (@user)
      session[:user_id]=@user.id
      redirect_to '/user/network'
    else
      flash[:errors] = @user.errors.full_messages
      redirect_to "/"
  end
end

  def create
    @user=User.create(name: params[:name], email: params[:email], password: params[:password], password_confirmation: params[:password_confirmation], description: params[:description])
  if @user.valid?
    session[:user_id]=@user.id
    redirect_to '/users/show'
  else
    flash[:errors] = @user.errors.full_messages
    redirect_to "/"
  end
end


  def delete
  end

  def show
    @user=User.find(params[:id])
  end

  def update
      @user = User.find(params[:id])
    if @user.update_attributes(name: params[:name], email: @user.email)
      puts @user.password
      puts "here!"
      redirect_to '/user/network'
    else
      flash[:errors] = @user.errors.full_messages
      redirect_to :back
    end


end

  def network
    @user=User.find(session[:user_id])
    @invitations=Invitation.where(user: @user)
    @network=Network.where(connection:@user)
    #puts "Jkjdslkfjdslkfjdslkfdjslkdfjslkfdsjlkfdsjl"* 100
  end
  def all
    @user=User.all
    @invitations=Invitation.where(user: @user)
    @network=Network.where(connection:@user)

  end
  def logout
    session.clear
    redirect_to "/"
  end

def user_params
params.require(:user).permit(:name, :email)

end
end
