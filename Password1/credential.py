from user import User
from random import choice # pick random in list to help in password generation
import string


class Credentials:
        '''
        this class will enable the generation of instance classes
        '''
        credential_list = []
        
        def __init__(self, credential_name, credential_password, user_account):
            """
            the _init_ method will define the properties of the User objects
        
            args:
            self.credential_password   = credential_password
            self.credential_name   = credential_name
            self.user_account   = user_account
            """
            
            
            self.credential_name = credential_name
            self.credential_password = credential_password
            self.user_account = user_account
          
        def save_credential(self):
            
            '''
            this is a methof that will save user's credentials
            '''
            
            Credentials.credential_list.append(self)
        
        
        def delete_credential(self):
            """
            it is a method to delete credentials
            """
            Credentials.credential_list.remove(self)
            
       
        @classmethod
        def show_credentials(cls,password):
            '''
            Method that returns the credential list
            Args:
            password : the user password
            '''
            user_credential_list = []
    
            for credential in cls.credential_list:
                if credential.credential_password == password:
                 user_credential_list.append(credential)
        
            return user_credential_list
            
        @classmethod
        def generate_password(cls):
            '''
            Method that generates a random alphanumeric password
            '''
        # Length of the generated password
            size = 8
    
            # Generate random alphanumeric 
            alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase
    
            # Create password
            password = ''.join( choice(alphanum) for num in range(size) )
        
            return password


            
        @classmethod
        def check_credentials(cls,name):
                """
                Method that checks if the credential of the user is available and return a boolean
                """
                credential_list = []    
            
            
                for credential in cls.credential_list:
                    if credential.credential_name == name:
                        return True