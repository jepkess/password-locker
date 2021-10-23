#!/usr/bin/env python3.8
from User import User, Details
# creating a new user
def create_user(username, password):
    """"
    method that creates a new user
    """
    new_user=User(username,password)
    return new_user

def save_user(user):
    """
    method that save the saves the user
    """ 
    user.save_user()
def display_user(user):
    """
    a method that displays already save user
    """
    return User.display_user(user)
           