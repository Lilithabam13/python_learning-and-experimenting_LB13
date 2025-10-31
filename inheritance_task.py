class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"
    
    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    # Method to display head office location
    def head_office(self):
        print("Head office location: Cape Town")


# Subclass with attributes at default values
class OOPCourse(Course):
    def __init__(self,description = "OOP Fundamentals",trainer = "Mr Anon A. Mouse"):
        super().__init__()
        self.description  = description
        self.trainer = trainer
    
    # method displaying what course is about as well as the trainer respectively
    def trainer_details(self):
        print(f"The course is about {self.description}\n with {self.trainer} as the trainer")

    # method displaying the course ID
    def show_course_id(self):
        print("The ID number of the course is #12345")

# Object of OOP course - which is a subclass of COURSE (class)
course_1 = OOPCourse()

# Displaying contact details (method of Parent Class), trainer and course ID details(methods of OOPCourse Class) respectively
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()

# Example usage:
# Create an instance of the Course class
course = Course()

# Call the contact_details method to display contact information
course.contact_details()
