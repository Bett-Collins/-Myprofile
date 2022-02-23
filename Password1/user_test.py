#!usr/bin/env python3.8
import unittest
from user import User 
from credential import Credentials


class TestUser(unittest.TestCase):
    
    '''
     This class defines test cases for the user class behaviour
    
    args:
    unittest.TestCase: it helps create test cases
    '''
     
    
    def setUp(self):
         '''
         setUp method enable test to be executed before each test
         '''
         
         self.new_user = User("Collins","Bett")
         
def tearDown(self):
             
             '''
                     tearDown method clean up after each test case is run
             '''
             User.user_list = []
             
def test_init(self):
                 
                 '''
                 test is used to see if the object has been initialized correctly
                 '''
                 self.assertEqual(self.new_user.user_name,"Collins")
                 self.assertEqual(self.new_user.user_password,"Bett")
                 
                 
def test_save_user(self):
                   
                   '''
                  find user using username 
                   ''' 
                
                   self.new_user.save_user()
                   self.assertEqual(len(User.user_list),1)
   
   
def test_show_user(self):
        '''
         This test method is to confirm if user_list is added
        '''
        
        self.assertEqual( User.show_user() , User.user_list )  
   
   
   
def test_sign_in(self):
        """
        This method test if the user is able to sign in to their account
        """
        self.new_user.save_user()
        test_user = User("Collins","Bett")
        test_user.save_user()
        found_credentials = User.sign_in("Collins","Bett")
        self.assertEqual(found_credentials, Credentials.user_credential_list)
 
   
   
   
   
   
   
   
   
             
               
def test_delete_user(self):
                 
                 '''
                 deleting user's details
                 '''
                
                 self.new_user.save_user()
                 test_user = User("Collins","Bett")
                 test_user.save_user()
                 self.new_user.delete_user()
                 self.assertEqual(len(User.user_list), 1) 
             


             
               
                 
if __name__ == '__main__':
    unittest.main()
