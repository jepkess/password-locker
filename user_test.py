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
        self.assertEqual(self.new_user.password,"jepkess1234") 

    def test_save_user(self): 
        """
        test case for checking if the new instances of the user object is save.

        """ 
        self.new_user.save_User() # saving the new contact
        self.assertEqual(len(User.user_list),1)
class TestDetails(unittest.TestCase):
        """
        class test that defines the testcases for the class details
        """ 
        def setUp(self):
            """
            a method that runs at the start of every test
            """
            self.new_details = Details("vincent","jep1234","1234jep")

        def tearDown(self):
            """
            method that clean up after each test has run
            """   
            Details.details_list=[]
        #checking for the expected results.
        def test_details(self):
            """
            method that check if the new details instances has been instancialized correctly.
            """
            self.assertEqual(self.new_details.account,"vincent")
            self.assertEqual(self.new_details.username,"jep1234")
            self.assertEqual(self.new_details.password,"1234jep")

        def test_save_details(self):
         """
         test case to test if the detail object is saved into the details list.
        """
         self.new_details.save_user_details()
         self.assertEqual(len(Details.details_list),1)

        def save_multiple_details(self): 
            """
            test for the save of the multiple account
            """
            self.new_details.save_user_Details()
            test_detail = Details("Ibrah","ibrah123","123ibrah")
            test_detail.save_User_Details()
            self.assertEqual(len(Details.details_list),2)
        def test_find_detail(self):
         """
        test to check if we can find a detail.
        """
        
         self.new_details.save_user_details()
         test_details = Details('Ibrah','ibrah123','123ibrah')
         test_details.save_user_details()

         the_detail = Details.find_by_number("ibrah123")
         self.assertEqual(the_detail.account,test_details.account)

        def test_detail_exist(self):
         """
        test to check if we can find the detail.
        """
         self.new_details.save_user_details()
         test_details = Details('Ibrah','ibrah123','123ibrah')
         test_details.save_user_details()
        
         find_detail = Details.details_exist("ibrah123")
         self.assertTrue(find_detail)
#method that test if we can remove an account detail.
        def test_delete_detail(self):
         """
        test method to test if we can remove an account details
        """
         self.new_details.save_User_Details()
         test_details = Details('Ibrah','ibrah123','123ibrah')
         test_details.save_user_details()
        
        
         self.new_details.delete_details()
         self.assertEqual(len(Details.details_list),1)

if __name__ == "__main__":
    unittest.main()        


