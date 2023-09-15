

students = {
    'Student1': {
       'Name': 'Hashim',
       'Age': '23',
       'Course': 'Artificial Intelligence',
    },

    'Student2': {
       'Name': 'Abdullsh',
       'Age': '24',
       'Course': 'Web Development',
    },

    'Student3': {
       'Name': 'Hameed',
       'Age': '23',
       'Course': 'Mobile App Development',
    },
}


def   delete_student(listt):
    std=str(input('Enter the name of student which you want to delete:'))
    for x in listt:
        if(listt[x] == std):
            listt.pop(x)
            print(f"Student '{x_name}' has been Removed")




def add_student(student_list):
    new_name = input('Enter the name of the student: ')
    new_age = input('Enter the age of the student: ')
    new_course = input('Enter the course name: ')

    new_student = {
        'Name': new_name,
        'Age': new_age,
        'Course': new_course,
    }

    new_student_key = 'Student' + str(len(student_list) + 1)

    # Add the new student to the dictionary
    student_list[new_student_key] = new_student

    print(f"Student '{new_name}' has been added as {new_student_key}.")


def show(listss):
   
    print("\nCurrent Student Dictionary:")
    for key, value in listss.items():
        print(f"{key}: {value}")
  

#print(students)

print('If you want to show The students data then press Show \n If you want to add a student data then press ADD \n If you want to Delete The students data then press Delete \n Enter a key (or \'quit\' to exit):  \n if you want to see a specific name type search')





while(1):
    choice=str(input('Tell me what you want:'))
    if(choice=='Show' or choice == 'show' ):
        show(students)

    elif(choice=='ADD' or choice == 'add'):
        add_student(students)
    
    elif(choice=='Delete' or choice == 'delete'):
        delete_student(students)
    

    elif(choice == 'quit'):
        break; 


