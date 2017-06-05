class Project
  # your code here
  attr_accessor :project, :description, :owner, :tasks
  attr_reader :tasks

def initialize (project, description, owner)
  @project= project
  @description  = description
  @owner= owner
  @tasks= []

end

def project_pitch
"Pitch: #{@project}, #{@description}"
end

def add_tasks tasks
  @tasks.push(tasks)
end


def get_tasks
for i in tasks
  puts i
end
end

end
#project1 = Project.new("Project 1", "Description 1", "Dan")
#project2 = Project.new("Project 2", "Description 2", "JimmyMixer")

#puts project1.project # => "Project 1"
#project1.project_pitch  # => "Project 1, Description 1"
#project2.project_pitch
