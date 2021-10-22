import random
import string
class User:
    """
    class that generates new instances of a user
    """
    User_list=[] # Empty user list
    def __init__(self,username,password): # init method allows us to  create a new instances of a class
        User.username=username
        User.password=password
    def save_User(self):
        """
        method that saves the user to the list
        """   
        User.user_list(self).append(self)
    def delete_User(self):
        """
        a method that delete saved user from the list
        """   
        User.user_list.remove(self) 

    @classmethod
    def display_user(cls):
        """
        method that displays the user in the users list
        """ 
        return cls.user_list

class Details:
    """
    class that generates an instance of an account details  and list of details
    """
    Details_list=[]
    def __init__(self, account,username,password):
        self.account = account
        self.username = username
        self.password = password
    @classmethod
    def verify_user(cls,username,password):
        a_user="" 
        for user in User.user_list: # for loop that loop into the user_list and and return a user when it finds.
            if(user.username == username and user.password == password):
                a_user == user.username
                return a_user

    def save_User_Details(self):
        """
        a method that saves the user details to the details list.
        """
        Details.details_list.append(self)

    def delete_details(self):
        """
        method that details the details in the details list
        """  
        Details.details_list.remove(self)

    @classmethod
    def find_by_number(cls, account):
        """
        a method that find account number and return the password that matches with the number
        """  

        for details in Details.details_listcls.credentials_list:
            if(details.account_number == account):
                return details 

    @classmethod
    def details_exists(cls,account):
        """
        this method checks whether the details in the details list exists and return 
        a boolean.
        """
        for detail in cls.details_list:
            if detail.account == account:
                return True
        return False
    def generates_password(self):
        """
        method that generates random password of mix letters and numbers
        """   
        password = string.ascii_uppercase + string.ascii_lowercase
        return ''.join(random.choice(password) for i in range(1,9))


   

            




        
          