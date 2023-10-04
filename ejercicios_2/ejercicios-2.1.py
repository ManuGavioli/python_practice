#The teacher of the class was missing so the students decided to do the set up (the oldest student is the teacher and the youngest is the assistant)

#Function to get the assistant and teacher based on the age
def get_students(quantity):
    #Creating the list of students
    students = []
    #Ask for the name and age of the students
    for i in range(quantity):
        name = input("Enter the name of the student: ")
        age = int(input("Enter the age of the student: ")) 
        student = (name,age)
        #Add the info to the list
        students.append(student)
    #Sort the students from youngest to aoldest by age 
    students.sort(key=lambda x:x[1])
    #Students[x] returns a tuple with (name,age) then we can access to the name to define the assistant and teacher
    assistant = students[0][0]
    teacher = students [-1][0]
    #Return the tuple
    return assistant, teacher

#Unpacking the data
assist,teacher = get_students(5)
#Print the result
print(f"The teacher is: {teacher} and his assistant is {assist}")