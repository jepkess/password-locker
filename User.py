class User:
    """
    class that generates new instances of a user
    """
    User_list=[] # Empty user list
    def __init__(self,username,password):
        User.username=username
        User.password=password
    def save_User(self):
        """
        method that saves the user to the list
        """   
        User.user_list(self).append(self)

        
          