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
