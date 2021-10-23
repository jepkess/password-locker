#!/usr/bin/env python3.8
from User import User, Details
# creating a new user
def create_user(username, password):
    """"
    Function that creates a new user
    """
    new_user=User(username,password)
    return new_user

def save_user(user):
    """
    Function that save the saves the user
    """ 
    user.save_user()
def display_user(user):
    """
    Function that displays already save user
    """
    return User.display_user(user)
    # verify the user login details
def login_user(password, username):
    """
    a function that if the user has already exists
    """  
    checked_user = Details.verify_user(password, username)
    return checked_user

    #creating new details

def create_new_detail(account,username,password):
    """
    a function that create new details.
    """ 
    new_detail= Details(account,username,password)  
    return new_detail

def save_details(details):
    """
    function that saves the created details
    """
    details.save_user_details()  

def delete_details(details):
    """
    a function that deletes the created details
    """
    details.delete_user_details 
    
def find_detail(account):
    """
    Function that finds a details by an account name 
    """
    return Details.find_by_number(account) 
def check_details(account):
    """
    a function that checks if the details of the searched name exist and return a true or false value.
    """
    return Details.details_exist(account) 
def generate_password(self):
    """
    a function that generates password randomly
    """
    auto_password = Details.generate_password(self)
    return auto_password

def main():
    print("Hello, welcome to password-locker.\n To proceed please enter the following short codes\n nw....create new account\n lg....Already have an account\n")
    short_code=input("").lower().strip()
    if short_code == 'nw':
        print("Register")
        print('*' * 50)
        print("Username")
        username = input()
        print("password")
        password = ""
        while True:
            print(" TP - type your own pasword?\n GP - generate  new Password")
            pass_choice = input().lower().strip()
            if pass_choice == 'tp':
                print("\n")
                password = input("Enter Password\n")
                break
            elif pass_choice == 'gp':
                password = generate_password(password)
            else:
                print("Invalid password")
        save_user(create_user(username,password)) # create and save new contact.
        print ('\n')
        print(f"Hello, {username} you have successfully created an account,your password is {password}")
        print ('\n')
    elif short_code == "lg":
        print("*"*20)
        print("Enter your User name and your Password to log in:")
        print('*' * 20)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password) 
    if login_user ==login:
        print(f"Hello,{username} ,Welcome to the passwordlocker App") 
        print("\n") 
    while True:
        print("To proceed select any:\n CD - Create a new detail  \n VD - View a detail \n GP - Generate a random password \n DEL - Delete detail \n EX - Exit the application \n")    
        short_code = input().lower().strip()
        if short_code == "cd":
            print("Create New Details")
            print("*"*20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            username = input()
        while True:
                print(" TP - Type your own pasword if you already have an account:\n GP - Generate a random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'gp':
                    password = generate_password(password)
                    break
                else:
                    print("Invalid password please try again")
                save_details(create_new_detail(account,username,password))
                print('\n')
                print(f"Account Details for:Account {account} :Username: {username} - Password:{password} was successfully created.")
                print('\n')   



if __name__=='__main__':
    main()




         
