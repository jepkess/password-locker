import unittest
from User import User
from User import Details
class TestUser(unittest.TestCase):
    def setUp(self):
        """
        A method that runs before the test starts
        """
        self.new_user = User("vincent","vinnie2021")

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        """
        test case to check if the object in initialized correctly
        """
        self.assertEqual(self.new_user.username,"vincent")
        self.assertEqual(self.new_user.password,"vinnie2021")
    
    def test_save_user(self):
        '''
        test case to check if the new instance of the user object has been created
        '''
        
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

class TestDetails(unittest.TestCase):
    """
    A test class that defines the test cases for the class details
    """
    def setUp(self):
        '''
         a method that runs before each individual details test methods run.
        '''
        self.new_details = Details("vincent","vinnie2021","2021vinnie")

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Details.details_list = []
    def test_details(self):
        """
        Test case to check if a new Details instance has been initialized correctly
        """
        self.assertEqual(self.new_details.account,"vincent")
        self.assertEqual(self.new_details.username,"vinnie2021")
        self.assertEqual(self.new_details.password,"2021vinnie")

    def test_save_details(self):
        """
        test case to test if the detail object is saved into the cdetails list.
        """
        self.new_details.save_user_details()
        self.assertEqual(len(Details.details_list),1)

    def test_save_many_account(self):
        '''
        test to check if we can save multiple details objects to our details list
        '''
        self.new_details.save_user_details()
        test_detail = Details("Ibrahim","Ibrah","ibrah3")
        test_detail.save_user_details()
        self.assertEqual(len(Details.details_list),2)

     
    def test_find_detail(self):
        """
        test to check if we can find a detail entry by account name and display it.
        """
        
        self.new_details.save_user_details()
        test_details = Details('Ibrahim','Ibrah','ibrah3')
        test_details.save_user_details()

        the_detail = Details.find_by_number("Ibrahim")
        self.assertEqual(the_detail.account,test_details.account)

    def test_detail_exist(self):
        """
        test to check if we can return a true or false based on whether we find or can't find the detail.
        """
        self.new_details.save_user_details()
        test_details = Details('Ibrahim','Ibrah','ibrah3')
        test_details.save_user_details()
        
        found_detail = Details.details_exist("Ibrahim")
        self.assertTrue(found_detail)

    def test_delete_detail(self):
        """
        test method to test if we can remove an account details from the list.
        """
        self.new_details.save_user_details()
        test_details = Details('Ibrahim','Ibrah','ibrah3')
        test_details.save_user_details()
        
        
        self.new_details.delete_details()
        self.assertEqual(len(Details.details_list),1)

if __name__ == '__main__':
    unittest.main()