import unittest
from User import User
from User import Details
class Testuser(unittest.TestCase):
    def setUp(self):
        """
        A method that runs before the test starts
        """
        self.new_user = User("vinnie","jepkess1234")

    def tearDown(self):
        """
         method that does clean up after each test case has run.
        """ 
        User.user_list = [] 
        #checking for the expected results
    def test_init(self):
        """
        test case to check if the object is initialized properly.
        """ 
        self.assertEqual(self.new_user.username,"vinnie") 
        self.assertEqual(self.new_user.password,"12345") 

    def test_save_user(self): 
        """
        test case for checking if the new instances of the user object is save.

        """ 
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.contact_list),1)
if __name__ == "__main__":
    unittest.main()        


