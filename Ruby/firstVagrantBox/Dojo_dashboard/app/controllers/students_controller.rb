class StudentsController < ApplicationController
  def index
  @dojo=Dojo.find(params[:dojo_id])
  @student=Student.where(dojo: @dojo)

  end

  def new
    @dojo=Dojo.find(params[:dojo_id])
    @dojos=Dojo.all
  end

  def shows
  end

  def delete
  end



  def create
    dojo= Dojo.find(params[:dojo])
    Student.create(first_name: params[:first], last_name: params[:lname], email:params[:email], dojo: dojo)



  redirect_to '/dojos/' + params[:dojo_id]+ '/students'
  end

  def edit
    @dojo=Dojo.find(params[:dojo_id])
    @student=Student.find(params[:id])
    @dojos=Dojo.all
    render '/students/edit'
  end
  def update
    @student= Student.find(params[:id])


    @dojo=Dojo.find(params[:dojo])
    puts @dojo
    @student.update(first_name: params[:first_name], last_name: params[:last_name], email: params[:email], dojo: @dojo)
    redirect_to '/dojos/' + params[:dojo]+ '/students'
  end

  #private
  #def student_params(dojo)
    #   params.require(:student).permit(:first_name, :last_name, :email, :dojo)
    # end
end
