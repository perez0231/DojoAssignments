
#
# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]



users = {
     'students': [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
      ],
     'Instructors': [
         {'first_name' : 'Michael', 'last_name' : 'Choi'},
         {'first_name' : 'Martin', 'last_name' : 'Puryear'}
      ]
     }

    # for value in users:
    #     print value['first_name'], value['last_name']

def names(users):
    for key, data in users.items():
        print key
        count = 0
        for value in data:
            count +=1
            print count, "-", value['first_name'], value['last_name'], "-", len(value['first_name'] + value['last_name'])


    # for data in students:
    #     print data

    #
    # for val in students.first_name():
    #     print val

names(users)
