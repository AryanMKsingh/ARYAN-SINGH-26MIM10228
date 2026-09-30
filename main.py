from time import *
from os import *

# db for projects
projData = {}

def cls():
    # clear screen
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def submit_project():
    print("\n-- Add a new project --")
    
    rno = input("Enter Registration Number: ")
    
    if rno=="":
        print("Registration number is required! Try again.")
        return

    if rno in projData:
        print("Looks like %s already submitted a project." % rno)
        return

    s_name = input("Enter Student Name: ")
    p_topic=input("Enter Project Topic: ")
    
    dt = input("Submission Date (DD-MM-YYYY): ")

    # save it
    projData[rno] = {
        "Name":s_name,
        "Topic":p_topic,
        "Date": dt,
        "Marks":"Not assigned yet"
    }
    
    print("\nSaving data...")
    sleep(1)
    print("Project saved successfully!")


def search_proj():
    print("\n-- Search Project --")
    rno = input("Enter the Registration Number to search: ")
    
    print("Searching...")
    sleep(0.5)
    print("\n")

    if rno in projData:
        rec=projData[rno]
        print("==============================")
        print("       PROJECT DETAILS        ")
        print("==============================")
        print("Reg Number :", rno)
        print("Name       :", rec['Name'])
        print("Topic      :", rec['Topic'])
        print("Date       :", rec['Date'])
        print("Marks      :", rec['Marks'])
        print("==============================")
    else:
        print("Sorry, no project found for this registration number.")


def grade_project():
    print("\n-- Assign Marks --")
    
    # check admin
    pwd=input("Admin Password: ")

    if pwd!="admin123":
        print("Wrong password! Access Denied.")
        return

    print("Login successful.")
    rno = input("Enter Registration Number to grade: ")

    if rno in projData:
        name=projData[rno]["Name"]
        score = input("Enter marks for %s: " % name)
        
        projData[rno]["Marks"]=score
        
        print("Saving marks...")
        sleep(0.5)
        print("Marks updated successfully!")
    else:
        print("No project found for this reg no.")


def view_all_projects():
    print("\nLoading all submissions...")
    sleep(1)

    if len(projData)==0:
        print("No projects have been submitted yet.")
        return

    print("\n*************************")
    print("    ALL SUBMISSIONS      ")
    print("*************************")

    for rno in projData:
        details = projData[rno]
        print("\nReg Number : %s" % rno)
        print("Name       : %s" % details['Name'])
        print("Topic      : %s" % details['Topic'])
        print("Date       : %s" % details['Date'])
        print("Marks      : %s" % details['Marks'])
        print("---------------------------------")


def main_menu():
    cls()
    print("Welcome to the Student Project Submission System")
    
    while True:
        print("\n==================================")
        print("         MAIN MENU                ")
        print("==================================")
        print("1. Add a new submission")
        print("2. Search for a submission")
        print("3. Assign marks (Admin only)")
        print("4. View all submissions")
        print("5. Exit system")
        
        c = input("\nEnter your choice (1-5): ")

        if c=="1":
            submit_project()
        elif c=="2":
            search_proj()
        elif c=="3":
            grade_project()
        elif c=="4":
            view_all_projects()
        elif c=="5":
            print("\nExiting the system. Have a great day!")
            sleep(0.5)
            break
        else:
            print("Invalid choice. Please select a valid option from 1 to 5.")
        
        # wait a bit
        sleep(1)

if __name__ == "__main__":
    main_menu()