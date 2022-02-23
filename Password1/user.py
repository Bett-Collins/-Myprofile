from credential import Credentials

class User:
    '''
    class will generate instance of user account
    '''
    user_list  =[]
   
    
def _init_(self,user_name,user_password):
        '''
        we define the property object by using _init_
        '''
        '''
         args:
        user.name: name of  a user
        user_password: password of the user
        '''
        
        self.user_name =user_name
        self.user_password = user_password
        
def save_user(self):
            '''
            this method will save the user list
            '''
            User.user_list.append(self)
            
            
@classmethod
def show_user(cls):
        '''
        Method that returns the user list
        '''
        
        return cls.user_list
            
@classmethod
def confirm_user(cls, user_name):
        """
        The method confirms if the details the user has entered is in the user_list
        """
        for user in cls.user_list:
            if user.user_name == user_name:
                return True
        return False   
        
        
       
@classmethod
     
def log_in(cls,user_name,user_password):
        """
        Method that will allow user to  login into their account
        """
        for user in cls.user_list:
            if user.user_name == user_name and user.user_password == user_password:
                return Credentials.user_credential_list
            return False
    
     
@classmethod
def delete_account(self,username):
        '''
        deletes saved account
        '''
        for user in User.user_list:
            if User.user_name == username:
                User.user_list.remove(user)

     
     