#The following program is a student registry 

#Prompt user for input into the no. of students
no_of_students = int(input("Please enter number of students: "))

#variable to store the IDs of the students 
list_of_no_of_students = []

#Loop through defined no. of students. Used range function because it helps define the no. of times we want to ask the students to enter their IDs. +1 because range starts at 0 but does not end at include the actual no. of students (Pythonic Rules)
for i in range(1, no_of_students + 1):
        
#Prompt students for IDs. Add each ID to list_of_no_of_students variable(container) to hold IDs. we can now manipulate the data
        list_of_no_of_students.append(str(input("Please enter your student_ID: ")))

#New-line special character for legibility and dots for student's signature
        print("\n")
        print("........................")

#opening new text file in write mode only
with open("reg_form.txt", "w") as file:

#looping through each itemn on file and printing it. Since we are creating the new text file it is still empty therefore we have to loop through the list_of_no_of_students variable(container) again to print each of the individual ID onto the txt tile      
        for i in list_of_no_of_students:
            file.write(i + "\n")
            print(i)
            


