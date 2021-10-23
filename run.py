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
def login_user(password, username):
    """
    a function that if the user has already exists
    """  
    checked_user = Details.verify_user(password, username)
    return checked_user
