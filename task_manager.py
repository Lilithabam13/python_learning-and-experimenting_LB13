# ===== Importing external modules ===========
'''This is the section where you will import modules'''
from datetime import datetime, date


def date_format(date_str):
    """Helper function to ensure date formatting
    Ensures system handles multiple date formats
    
    Args:
        date_str(str): String task date
    
    Returns:
        Python date object
    """
    for fmt in ("%Y-%m-%d", "%d %b %Y"):
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Date: {date_str} is an unrecognized format. ")


# ==== Login Section ====
# Login user
def login(users_list):
    """Login/Sign-in user into the system
    
    Args:
        users_list (list): List of User objects
    
    Returns:
        User object: User object in the system/list
    """
    while True:
        print("\n" + "-"*40)
        login_username = input("Please enter your username: ").strip().lower()
        login_password = input("Please enter password: ").strip().lower()
            
        logged_in_user = next((user for user in users_list if user.username == login_username),None)
        
        if logged_in_user:
            if logged_in_user.password == login_password:
                print (f"Login Successful, Welcome {logged_in_user.username}")
                return logged_in_user
            else:
                print("Password is incorrect, please try again")
        
        else:print("Username is not registered on system, please try again")

# ------------- CLASSES -------------

class User():
    """Represents a user in the system.
    
    Attributes:
        username (str): Name of user
        password (str): Password of user
        tasks (list): List of tasks assigned to user
    
    Methods:
        _str_ : String representation of user
        users_input: Prompt user for valid username and password
    """
    def __init__(self, username = None, password = None):
        self.username = username
        self.password = password
        self.tasks = []
        

    # String representation
    def __str__(self):
        return ("-----User Details-----\n"   
        f"Username: {self.username}\n"
        f"Password: {self.password}\n"
        )
    
    # Input method
    def users_input(self):
        """Prompt user to enter valid username and password
        
        Username must only be letters
        Password must be alphanumeric
        """
        # Valid username
        while True:
            print("\n")
            self.username = input("Please enter username: ").strip().lower()
            if self.username.isalpha():
                break
            else:
                print("Invalid username, please try again")
        
        # Valid password
        while True:
            print("\n")
            self.password = input("Please enter password: ").strip().lower()
            if self.password.isalnum():
                break
            else:
                print("Invalid password, please try again")


class Task():
    """Represents a task in the system.
    
    Attributes:
        user (User): User assigned to a task
        title (str): Title of task
        description (str): Description of task
        date_assigned (date): Date task was issued to a user
        due_date (date): Due date of task
        completed (str): Completion status of task
        
    Methods:
        _str_: String representation of a task
        task_complete(): Update completion status of task
        task_input(): Prompt user to create a task
        view_user_task(): Enables user to view task assigned to them 
    """
    def __init__(self, user = None, title = None, description = None, date_assigned = None, due_date = None, completed="No"):
        self.user = user
        self.title = title
        self.description = description
        self.date_assigned = datetime.strptime(date_assigned,"%Y-%m-%d").date() if isinstance(date_assigned,str) else date_assigned
        self.due_date = datetime.strptime(due_date,"%Y-%m-%d").date() if isinstance(due_date,str) else due_date
        self.completed = completed  
              
        if self.user is not None:
            self.user.tasks.append(self)
    
    # Updaate completion status
    def task_complete(self):
        """Updates task completion status

        """
        self.completed = "No" if self.completed == "Yes" else "Yes"
        print(f"Task completion status changed to {self.completed}")
    
    # String representation
    def __str__(self):
        return ("-----Task Details-----\n"  
        f"Task: {self.title}\n" 
        f"Assingned to: {self.user.username}\n"
        f"Date_assigned: {self.date_assigned}\n"
        f"Due date: {self.due_date}\n"
        f"Completed: {self.completed}\n"
        f"Description: \n{self.description}")
    
    # Input method
    def task_input(self):
        """Prompt user to enter a task's details.
        
        Only users within system may create task.
        
        Task dates (date_assigned,due_date) must date objects 
        Completion status is default to 'No'
        Title, description can not be empty
        """
        
        # Valid username
        while True:
            print("\n" + "-"*40)
            username = input("Please enter the name of user to assign task to: ").strip().lower()
            specific_user = next((user for user in users_list if user.username == username), None)
            if specific_user:
                self.user = specific_user
                break
            print(f"{username} is not registered on the system, please try again")
        
        # Valid title
        while True:
            print("\n" + "-"*40)
            self.title = input("Please enter the title of the task: ").strip()
            if self.title:
                break
            else:
                print("Title can not be empty, please try again")
        
        # Valid description
        while True:
            print("\n" + "-"*40)
            self.description = input("Please enter the description of the task: ").strip()
            if self.description:
                break
            else:
                print("Description can not be empty, please try again")
        
        # Valid date assigned
        self.date_assigned = date.today()

        # Valid due_date
        while True:
            print("\n" + "-"*40)
            self.due_date = input("Please enter the due date (YYYY-MM-DD): ").strip()
            try:
                self.due_date = datetime.strptime(self.due_date,"%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid format, please try again (eg. 2025-06-18).")

        # Completed
        self.completed = "No"

    
    def view_user_task(self):
        """Enable user to view their specific task(s)

        Only users within system may view their task(s)

        Only 'admin' users are able to edit task details
        such as assignment and due date
        """
        username = input("Please enter your username: ").strip().lower()
        
        for user in users_list:
            if user.username == username:
                users_tasks = user.tasks
                view_tasks(user.tasks)
                
                while True:
                    print("\n")
                    try:
                        specific_task = int(input("Select a specific task to edit -1(by entering a number) or -1 to return to the main menu: "))
                        
                        if specific_task == -1:
                            
                            print("Returning to main menu")
                            return
                        
                        if 1 <= specific_task <= len(users_tasks):
                            for index, task in enumerate(users_tasks,start=1):
                                if specific_task == index:
                                    print(f"You have selected {specific_task}")
                                    print(task)
                                    
                                    # Edit task completion strtus
                                    while True:
                                        task_completion = input("Task complete? (yes/no): ").strip().lower()
                                        if task_completion == "yes":
                                            task.completed = "Yes"
                                            break
                                        elif task_completion == "no":
                                            task.completed = "No"
                                            break
                                        else:
                                            print("Invalid entry. Please enter 'Yes' or 'No'")
                                        
                                    print(f"Task {task} status updated to: {task.completed} ")
                                    edit_task(task)
                                    view_tasks(user.tasks)
                                    break

                            # To contiune    
                            while True:
                                reloop = input("Do you wish to edit another task (Yes/No): ").strip().lower()
                                if reloop == "yes":
                                    break
                                elif reloop == "no":
                                    return
                                else:
                                    print("Invalid entry. Please enter 'Yes' or 'No'")
                        else:
                            print(f"Task No.{specific_task} is out of range. Please try again")
                    
                    except ValueError:
                        print("Invalid entry.. please enter a number (1,2,3,4 etc.)")
        else:
            print(f"No task was found under {username}. Please try again")


# ------------- GLOBAL DATA -------------
"""Used to store list of objects of User/Task class respectively
"""
users_list = []
tasks_list = []

# ------------- FILE READING -------------
def read_user_data():
    """Load user data from 'user' text file into user objects.

    Returns:
    users_list (list): List of User objects 
    """
    try:
        with open("user.txt", "r") as file:
            for line in file:
                username, password = [item.strip() for item in line.split(",")[:2]]
                users_list.append(User(username, password))
                print("Debug Users:",[(user.username, user.password) for user in users_list])

    except FileNotFoundError:
            print("The file does not exist. Please check the file path and try again")
    return users_list  

def read_task_data():
    """Load user data from 'tasks' text file into task objects

    Returns:
        tasks_list (list): List of Task objects 
    """
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                username, title, description, date_assigned, due_date, completed = [item.strip() for item in line.split(",")[:6]]
                date_assigned = date_format(date_assigned)
                due_date = date_format(due_date)

                specific_user = next((user for user in users_list if user.username == username), None) 
                
                if specific_user:
                    tasks_list.append(Task(specific_user, title, description, date_assigned, due_date, completed))
    
    except FileNotFoundError:
            print("The file does not exist. Please check the file path and try again")
    return tasks_list  

# ------------- TASK MANAGER FUNCTIONS -------------

# Register new user        
def register_user(users_list):
    """Register a new user into the system and save it to user.txt file
    
    User is prompted to enter new username and password.

    Args:
        users_list (list): List of User objects

    Returns:
        users_list (list): Updated list of User objects, includes new user
    """
    while True:
        new_user = User()
        new_user.users_input()
    
        if any(user.username == new_user.username for user in users_list):
            print(f"{new_user.username} is already registered")
            continue

        confirmed_password = input("Please confirm password:").strip().lower()
        if confirmed_password == new_user.password:
            users_list.append(new_user)
            with open("user.txt","a") as file:
                file.write(f"{new_user.username}, {new_user.password}\n")
                print("Successful registration")
                return users_list
        else:
            print("Passwords do not match, please try again")

# Add new task        
def add_task(tasks_list):
    """Add a new task into the system and save it to tasks.txt file.
    
    User is prompted to enter task details.

    Args:
        tasks_list (list): List of Task objects

    Returns:
        tasks_list (list): Updated list of Task objects, includes new task.
    """
    new_task = Task()
    new_task.task_input()
    
    tasks_list.append(new_task)

    with open("tasks.txt","a") as file:
        file.write(f"{new_task.user.username},{new_task.title},{new_task.description},{new_task.date_assigned},{new_task.due_date},{new_task.completed}\n")
        print("Task added successful! ")
        return tasks_list

# Edit task
def edit_task(task):
    """Edit an existing task's details.
        Task title and and who the user (username of person assigned) of the task.
        Only incomplete tasks can be edited.

    Args:
        task (object): A task that is to be edited

    Displays updated task details in a legible manner (user-friendly).
    """
    if task.completed == "No":
        while True:
            print(f"'{task.title}' is currently assigned to {task.user.username}")
            edit_user = input(f"Do you wish to edit the task assignment from {task.user} (yes/no): ").strip().lower()
            
            if edit_user == "no":
                break
            
            elif edit_user == "yes":
                new_user = input("Enter name of person to assign task to: ").strip().lower()
                found_user  = next((user for user in users_list if user.username == new_user),None)
                if found_user:
                    task.user = found_user
                    print(f"The task: {task.title} has been successfuly assigned to {found_user.username}.")
                else:
                    print(f"The username: {new_user} is not registered on the system. ")
                break

            else:
                print("Invalid entry. Please enter 'yes' or 'no'")
    # Due date 
    while True:
        print(f" Task: '{task.title}' is due date on: {task.due_date}")
        edit_date = input(f"Do you wish to edit the due date of the task (yes/no): ").strip().lower()
               
        if edit_date == "no":
            print("OK thanks")
            break

        elif edit_date == "yes":
            while True:
                new_date = input("Enter the new due date (YYYY-MM-DD): ").strip()
                try: 
                    new_date = datetime.strptime(new_date,"%Y-%m-%d").date()
                    task.due_date = new_date
                    print(f"Task: '{task.title}' is now due on '{task.due_date}'")
                    break
                except ValueError:
                    print("Invalid format, please try again (eg. 2025-06-18).")
            break
        else:
            print("Invalid entry. Please enter 'yes' or 'no'")
    
    print("-----Updated Task Details-----\n"  
        f"Task: {task.title}\n" 
        f"Assigned to: {task.user.username}\n"
        f"Date_assigned: {task.date_assigned}\n"
        f"Due date: {task.due_date}\n"
        f"Completed: {task.completed}\n"
        f"Description: \n{task.description}")
    
# Delete task
def delete_task(logged_in_user):
    """Delete a task from system.
    Deleted task is saved to tasks.txt file
    
    Only 'admin' users are permitted to delete a task.
    
    Args:
        logged_in_user (User): A currently signed-in User object.

    Returns:
        tasks_list (list): Updated list of Task objects, excludes deleted task.
    """
    if logged_in_user.username == "admin":
        view_tasks(tasks_list)
        
        while True:
            try:
                deleted_task = int(input("which task do you wish to delete: "))
                if 1 <= deleted_task <= len(tasks_list):
                    for index, _ in enumerate(tasks_list,start=1):
                        if deleted_task == index:
                            removed_task = tasks_list.pop(index - 1)
                            print(f"Task: '{removed_task.title}'\n has been deleted.") 
                            
                            with open("tasks.txt","w") as file:
                                for t in tasks_list:
                                    file.write(f"{t.user.username},{t.title},{t.description},{t.date_assigned},{t.due_date},{t.completed}\n")   
                    break
                else:
                    print(f"Task No.{deleted_task} is not on the system.")
            except ValueError:
                print("Oops... Please enter a valid number.")
    else:
        print("'Admin members permitted to delete task only.'")
    return tasks_list

# View all tasks
def view_tasks(tasks_list):
    """Displays all the tasks in the system.
    
    Uses _str_ method of Task class to display task details in
    user-friendly format.
    
    Args:
        tasks_list (list): List of Task objects.
    """
    print("\n-----Tasks in Database-----")
    for index,task in enumerate(tasks_list,start=1):
        print(f"Task: {index}\n{task}")
        print("-"*40)
            
# View completed tasks
def view_completed(logged_in_user):
    """Displays all the completed tasks in the system.
    
    Only 'admin' users may view completed tasks.
    
    Args:
        logged_in_user (User): A currently signed-in User object.
    """
    if logged_in_user.username == "admin": 
        completed_tasks = [task for task in tasks_list if task.completed.lower() == "yes"]
        
        if completed_tasks:
            view_tasks(completed_tasks)

        else:
            print("No tasks have been completed yet.")
    else:
        print("This operation is for admin members only")

# ------------- REPORTS AND STATISTICS -------------

def generate_reports(users_list,tasks_list):
    """Generates and displays task/user specific report in respsective text files.

    Only 'admin' user may generate reports
    
    Task details are saved to task_overview.txt file.
    User details are saved to user_overview.txt file.
    
    Args:
       users_list (list): List of User objects.
       tasks_list (list): List of Task objects.
    """
    # Task overview
    if tasks_list:
        total_no_tasks = len(tasks_list)
        no_completed_tasks = sum(1 for task in tasks_list if task.completed.lower() == "yes")
        no_uncompleted_tasks = sum(1 for task in tasks_list if task.completed.lower() == "no")
        no_uncompleted_overdue_tasks = sum(1 for task in tasks_list if task.completed.lower() == "no" and task.due_date < date.today())
        percentage_incomplete_tasks= round((no_uncompleted_tasks/total_no_tasks)*100,2)
        percentage_overdue_tasks = round(((sum(1 for task in tasks_list if task.due_date < date.today())/total_no_tasks)*100),2)
        
        task_data = ("-----Task Overview Details-----\n"  
        f"Total number of tasks: {total_no_tasks}\n" 
        f"Total number of completed tasks: {no_completed_tasks}\n"
        f"Total number of uncompleted tasks: {no_uncompleted_tasks}\n" 
        f"Total number of uncompleted and overdue tasks: {no_uncompleted_overdue_tasks}\n" 
        f"Percentage of incomplete tasks: {percentage_incomplete_tasks} %\n" 
        f"Percentage of overdue tasks: {percentage_overdue_tasks} %")
    
    else:
        task_data = ("Task data could not be retrieved")
        return

    # User overview
    username = input("Enter a user's username to generate report: ").strip().lower()
    users_tasks = [task for task in tasks_list if task.user.username == username]
    
    total_no_users = len(users_list)
    total_no_tasks = len(tasks_list)
    user_total_tasks = len(users_tasks)
    percentage_user_tasks = round((user_total_tasks/total_no_tasks)*100,2)

    if len(users_tasks) == 0:
        print("User data could not be retrieved") 
        return

    else:
        percentage_user_completed_tasks = round(((sum(1 for task in users_tasks if task.completed.lower() == "yes")/user_total_tasks)*100),2)
        percentage_user_uncompleted_tasks = round(((sum(1 for task in users_tasks if task.completed.lower() == "no")/user_total_tasks)*100),2)
        percentage_user_uncompleted_overdue_tasks = round(((sum(1 for task in users_tasks if task.completed.lower() == "no" and task.due_date < date.today())/user_total_tasks)*100),2)

        user_data = ("-----Users Overview Details-----\n"  
        f"Total number of users: {total_no_users}\n"
        f"Total number of tasks: {total_no_tasks}\n" 
        f"Percentage of tasks assigned to {username}: {percentage_user_tasks} %\n"
        f"Percentage of completed tasks assigned to {username}: {percentage_user_completed_tasks} %\n" 
        f"Percentage of uncompleted tasks assigned to {username}: {percentage_user_uncompleted_tasks} %\n" 
        f"Percentage of uncompleted and overdue tasks assigned to {username}: {percentage_user_uncompleted_overdue_tasks} %"
        )

    with open("task_overview.txt","w+") as task_file:
        task_file.write(task_data)

    with open("user_overview.txt","w+") as user_file:
        user_file.write(user_data)

def display_statistics(users_list,tasks_list):
    """Generates and displays task/user report.

    Only 'admin' user may display statistics

    Calls task_overview() and user_overview() functions

    Args:
       users_list (list): List of User objects.
       tasks_list (list): List of Task objects.
    """
    task_overview(tasks_list)
    user_overview(users_list,tasks_list)

# Task overview
def task_overview(tasks_list):
    """Displays a summary of tasks in system.
    
    Highlights the total number of tasks as well as 
    completed tasks, uncompleted tasks, percentages of 
    incomplete and overdue tasks
    
    Args:
        tasks_list (list): List of Task objects
    """
    if tasks_list:
        total_no_tasks = len(tasks_list)
        no_completed_tasks = sum(1 for task in tasks_list if task.completed.lower() == "yes")
        no_uncompleted_tasks = sum(1 for task in tasks_list if task.completed.lower() == "no")
        no_uncompleted_overdue_tasks = sum(1 for task in tasks_list if task.completed.lower() == "no" and task.due_date < date.today())
        percentage_incomplete_tasks= round((no_uncompleted_tasks/total_no_tasks)*100,2)
        percentage_overdue_tasks = round(((sum(1 for task in tasks_list if task.due_date < date.today())/total_no_tasks)*100),2)
        
        print("-----Task Overview Details-----\n"  
        f"Total number of tasks: {total_no_tasks}\n" 
        f"Total number of completed tasks: {no_completed_tasks}\n"
        f"Total number of uncompleted tasks: {no_uncompleted_tasks}\n" 
        f"Total number of uncompleted and overdue tasks: {no_uncompleted_overdue_tasks}\n" 
        f"Percentage of incomplete tasks: {percentage_incomplete_tasks} %\n" 
        f"Percentage of overdue tasks: {percentage_overdue_tasks} %")
    
    else:
        print("No tasks in the system")
        return

# User overview
def user_overview(users_list,tasks_list):
    """Displays a summary of users in system.
    
    Highlights the total number of users as well as 
    completed tasks, uncompleted tasks, percentages of 
    incomplete and overdue tasks.
    
    Args:
        tasks_list (list): List of Task objects
    """
    username = input("Enter a user's username to generate report: ").strip().lower()
    users_tasks = [task for task in tasks_list if task.user.username == username]
    
    total_no_users = len(users_list)
    total_no_tasks = len(tasks_list)
    user_total_tasks = len(users_tasks)
    percentage_user_tasks = round((user_total_tasks/total_no_tasks)*100,2)

    if len(users_tasks) == 0:
        print("Tasks could not be accessed")

    else:
        percentage_user_completed_tasks = round(((sum(1 for task in users_tasks if task.completed.lower() == "yes")/user_total_tasks)*100),2)
        percentage_user_uncompleted_tasks = round(((sum(1 for task in users_tasks if task.completed.lower() == "no")/user_total_tasks)*100),2)
        percentage_user_uncompleted_overdue_tasks = round(((sum(1 for task in users_tasks if task.completed.lower() == "no" and task.due_date < date.today())/user_total_tasks)*100),2)

        print("-----Users Overview Details-----\n"  
        f"Total number of users: {total_no_users}\n"
        f"Total number of tasks: {total_no_tasks}\n" 
        f"Percentage of tasks assigned to {username}: {percentage_user_tasks} %\n"
        f"Percentage of completed tasks assigned to {username}: {percentage_user_completed_tasks} %\n" 
        f"Percentage of uncompleted tasks assigned to {username}: {percentage_user_uncompleted_tasks} %\n" 
        f"Percentage of uncompleted and overdue tasks assigned to {username}: {percentage_user_uncompleted_overdue_tasks} %"
        )

# Menu
def menu(logged_in_user):
    """Display user's option with regards
    to overall program.
    
    What a user sees is dependant on role within team.

    Args:
        logged_in_user (User): A currently signed-in User object.
    
    Returns:
        user_choice (str): Controls program flow.
    """

    if logged_in_user.username == "admin":
            print("\n")
            user_choice = input( '''\nSelect one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
vc - view completed
del - delete task
ds - display statistics                                                                  
gr - generate reports                              
e - exit : ''').strip().lower()
            
    
    else:
        print("\n")
        user_choice = input( '''\nSelect one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit : ''').strip().lower()
    
    return user_choice
 
# ------------- MENU (Program flow) -------------

users_list = read_user_data()
tasks_list = read_task_data()

current_user = login(users_list)

while True:
    user_choice = menu(current_user)

    if user_choice == 'r':
        users_list = register_user(users_list)


    elif user_choice == 'a':
        tasks_list = add_task(tasks_list)

    elif user_choice == 'va':
        view_tasks(tasks_list)
 

    elif user_choice == 'vm':
        view_my_tasks = Task()
        view_my_tasks.view_user_task()

    elif user_choice == 'vc':
        view_completed(current_user)
    
    elif user_choice == 'del':
        delete_task(current_user)
    
    elif user_choice == 'ds':
        display_statistics(users_list,tasks_list)
    
    elif user_choice == 'gr':
        generate_reports(users_list,tasks_list)

    elif user_choice == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")

