#!/usr/bin/env python3.8
from User import User,Details
def create_new_user(username,password):
    """
    function that creates a user using a password and username
    """
    new_user = User(username,password) 
    return new_user

def save_user(user):
    """
    function that saves a new user
    """
    user.save_user()

def display_user(user):
    """
    function that displays user
    """
    return User.display_user()

def login_user(password,username):
    """
    a function that checks if the users already exist 
    """
    checked_user = Details.verify_user(password,username)
    return checked_user

def create_new_detail(account,username,password):
    """
    function that create new details information for a new user
    """
    new_detail = Details(account,username,password)
    return new_detail

def save_details(details):
    """
    a function that saves a new detail information.
    """
    details.save_user_details()

def delete_details(details):
    """
    a function that deletes detailsfrom the  list
    """
    details.delete_details()

def find_detail(account):
    """
    Function that finds a details by an account name.
    """
    return Details.find_by_number(account)

def check_details(account):
    """
    a function that checks if the details of the searched name exist and return true or false
    """
    return Details.details_exist(account)

def generate_password(self):
    """
    a function that generates random password.
    """
    auto_password = Details.generate_password(self)
    return auto_password

def main():
    print("Hello user, Welcome to PasswordLocker.\n To procced enter any of the following short codes\n nw ---  To create a new Account  \n lg --- Already have An Account  \n")
    short_code = input("").lower().strip()
    if short_code == 'nw':
        print("Register Here")
        print('*' * 40)
        print("Username")
        username = input()
        print("password")
        password = ""
        while True:
            print(" TP - Type your own pasword?\n GP - Generate a random Password")
            pass_choice = input().lower().strip()
            if pass_choice == 'tp':
                print("\n")
                password = input("Enter Password\n")
                break
            elif pass_choice == 'gp':
                password = generate_password(password)
                break
            else:
                print("Invalid password")
        save_user(create_new_user(username,password))
        print("*"*60)
        print(f"Hello {username}, Your account has been created, Your password is: {password}")
        print("*"*60) 
    elif short_code == "lg":
        print("*"*50)
        print("Enter your User name and your Password to log in:")
        print('*' * 40)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username} welcome to PasswordLocker" )
            print("\n")
    while True:
        print("To proceed select any:\n CC - Create a new detail  \n VC - View a detail \n GP - Generate a randomn password \n DEL - Delete detail \n EX - Exit the application \n")    
        short_code = input().lower().strip()
        if short_code == "cc":
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
            print(f"Account Detail for:Account {account} :Username: {username} - Password:{password} created succesfully")
            print('\n')
        elif short_code == "vc":
            print("Enter the Account Name detailyou want to view")
            search_name = input().lower()
            if find_detail(search_name):
                search_detail = find_detail(search_name)
                print(f"Name : {search_detail.username}")
                print('*' * 40)
                print(f"User Name: {search_detail.username} Password :{search_detail.password}")
                print('*' * 40)
            else:
                print("That Detail does not exist")
                print('\n')
        elif short_code == "del":
            print("Enter account name of the Details you want to delete")
            search_name = input().lower()
            if find_detail(search_name):
                search_detail = find_detail(search_name)
                print("_"*40)
                search_detail.delete_details()
                print('\n')
                print(f"Your stored details for : {search_detail.account} has been successfully deleted!!!")
                print('\n')
            else:
                print("The Detail you want to delete does not exist")

        elif short_code == 'gp':

            password = generate_password(password)
            print(f" {password} Successful. ")
        elif short_code == 'ex':
            print("Thanks for using PasswordLocker.")
            break
        else:
            print("Wrong entry!!!Check your entry again")
    else:
        print("Please enter a valid input to continue")

if __name__ == '__main__':
    main()
         
