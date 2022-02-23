import unittest
from credential import Credentials
import random
import string



class TestCredentials(unittest.TestCase):
    
    '''
    Test class will define test case for class Credential behavior
    
    Args:
     TestCase class helps create test classes
    '''
    def setUp(self):
    
        '''
        setUp method runs before each test case 
        '''
    
    #Create Credential object
    
        self.new_credential = Credentials('arapbett','2030','facebook')

    def tearDown(self):
        '''
        tearDown method clean up after each test case is run
        '''
        Credentials.credential_list = []
        
    def test_init_(self):
            
        """
        Test case to check if a new Credentials have been initiated properly 
        """
        self.assertEqual(self.new_credential.credential_name,'arapbett')
        self.assertEqual(self.new_credential.credential_password,'2030')
        self.assertEqual(self.new_credential.credential_account,'facebook')
        
       
   
   
    def test_save_credential(self):
        """
        test case to test if the crential object is saved into the credentials list.
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credential_list),1)
        
        
        
        (Credentials.find_credentials(), Credentials.user_credential_list)
        
    def test_generate_password(self):
        '''
        Test case to determine if the user can log into their credentials
        '''
        
        generated_password = self.new_credential.generate_password()

        self.assertEqual(len(generated_password), 8 )      
        
        
    def test_check_credentials(self):
        
        '''
        The test test if it will return a boolean if the credential is absent
        '''

        
        self.new_credential.save_credential()

        test_credential = Credentials("arapbett","2030","facebook")

        test_credential.save_credential()
        
      
        credential_exists = Credentials.credential_exist("Facebook")
        
        self.assertTrue(credential_exists)
       
       
       