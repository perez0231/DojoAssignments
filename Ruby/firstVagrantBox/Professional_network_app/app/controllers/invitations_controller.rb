class InvitationsController < ApplicationController
  def index
  end

  def create
    user=User.find(session['user_id'])
    invitee=User.find(params[:id])
    Invitation.create(user: invitee, inviter: user)
    redirect_to :back
  end

  def destroy
    Invitation.find_by(inviter: params[:id]).destroy
    redirect_to :back
  end
end
