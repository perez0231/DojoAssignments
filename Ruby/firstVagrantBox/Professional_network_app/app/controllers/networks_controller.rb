class NetworksController < ApplicationController
  def new
  end

  def create

    user=User.find(session['user_id'])
    contact=User.find(params[:id])
    Network.create(connection: user, user: contact)
    Network.create(connection: contact, user: user)
    redirect_to "/invitations/delete"

  end

  def delete
  end
end
