# Email Program
inbox = []  

# Menu to prompt user 
menu_2 = {1:"Read an email",
                   2:"View unread emails",
                   3:"Quit application"
                   }

# Email class - with 4 instance variables  - defining what an object(email) is
class Email():
    def __init__(self,email_address,subject_line,email_content,has_been_read = False):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = has_been_read
    
# Update the status of email
    def mark_as_read(self):
        self.has_been_read = True

# Officially defining our object (email) and appending it to an empty list
def populate_inbox(email_address,subject_line,email_content):
    new_email = Email(email_address,subject_line,email_content)
    inbox.append(new_email)
        
# Lists each of the subject line of the emails(objects) with their corresponding indexes, respectively ie 1. Submission
def list_emails(inbox):
    for i, mail in enumerate(inbox):
        print (i, mail.subject_line)
      
# Displays the mail (oject) & its details while marking that mail as read. Mail displayed is dependant on user input
def read_email(inbox, index):
    email  = inbox[index]
    print(email.email_address, email.subject_line,email.email_content)
    print(f"Sender: {email.email_address}")
    print(f"Subject: {email.subject_line}")
    print(f"Content: {email.email_content}")
    email.mark_as_read()

        
while True:

# Printing Menu2 
    print("\nSelect an option from the menu below")
    for key,value in menu_2.items():
        print(f"{key}. {value}")
    
    # Prompting user for input
    try:
        user_choice = int(input("Please select the number of the next operation"))
    
    # In the event user enters a string as opposed to an integer  
    except ValueError:
        print("Please enter a valid option")
        continue

# User chooses to read an email
    if user_choice == 1:
        list_emails(inbox)
        try:
            
            user_input = int(input("Please enter the index of mail you want read: "))
            if 0 <= user_input <= len(inbox)-1:
                read_email(inbox,user_input)
        
        except ValueError:
            print("Please enter a valid number")

# User choosed to view all the unread emails
    elif user_choice == 2:
        unread_emails = [(i,mail) for i, mail in enumerate(inbox) if not mail.has_been_read]

        if not unread_emails:
            print("No unread mails")
            
        else:
            for i, mail in unread_emails:
                print(f"{i}. {mail.subject_line} from {mail.email_address}")

            try:
                user_input = int(input("Please enter the index of mail you want read: "))
                if user_input in [i for i, _ in unread_emails]:
                    read_email(inbox,user_input)

            except ValueError:
                print("Please enter a valid number")    
        
# User opts to exit application        
    elif user_choice == 3:
        print("Thanks for participating")
        break