require_relative 'project' # include our Project class in our spec file

RSpec.describe Project do
before (:each) do
  @project1 =Project.new('Project 1', 'Description 1', "Dan") # create a new project and make sure we can set the name attribute
  @project2 =Project.new('Project 2', 'Description 2', "JimmyMixer")

end
it 'has a getter and setter for name attribute' do

   @project1.project = "Changed Name" # this line would fail if our class did not have a setter method
   @project2.project = "Changed Name"
   expect(@project1.project).to eq("Changed Name") # this line would fail if we did not have a getter or expect(@project1.project).to eq("Changed Name")if it did not change the name successfully in the previous line.
   expect(@project2.project).to eq("Changed Name")
 end

 it 'has a getter and setter for the owner attribute' do
   expect(@project1.owner="Dan")
 end

it 'has a method project_pitch to explain name and description' do
   expect(@project1.project_pitch).to eq("Pitch: Project 1, Description 1")
   expect(@project2.project_pitch).to eq("Pitch: Project 2, Description 2")
 end

 it 'has a task and add' do
   @project1.add_tasks("poop")
   @project1.add_tasks("pee")
   expect(@project1.get_tasks).to eq(["poop", "pee"])
 end





end
