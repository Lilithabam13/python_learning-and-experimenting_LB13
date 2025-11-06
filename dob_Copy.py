
#Following program reads text file output Name and DOB accordingly
#*Best to break it up into parts as its easier to work with*

#Initiate empty list to store texts as string in list  - loop through list to ensure we are looping through each line as opposed to each character
records = []
#To hold Name data - as string
Name = []
#To hold Birthdate data - as string
Birthdate = []

#open text file in read only mode
with open("DOB.txt", "r") as file:

#loop through each line in the text file    
    for line in file:

#each line in file is held under 'records' - where it is stripped of white spaces & split into parts, starting from the Right to ensure the first 3 elements are the DOB
        records = (line.strip().rsplit(" ",3))

#split name - surname and DOB into variables. string has been spilt into 4 parts. without specifying the maxsplit string is split into individual elements
        name = records[0] # indexing first element
        birthdate = " ".join(records[1:]) # Joining elements of DOB via space.Indexing starting from second element   

#Add/append name into Name[] variable
        Name.append(name)
#Add/append birthdate into Birthdate[] variable       
        Birthdate.append(birthdate)


#Looping through each Name on text file and printing
print("Name:")
for i in Name:
    print(i)

#Printing space for legibility
print(" ")

#Looping through each Birthdate on text file to corresponding Name and printing
print("Birthdate:")
for i in Birthdate:
    print(i)    


