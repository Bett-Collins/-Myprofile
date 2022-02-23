from user import User
from credential import Credentials

def create_user(user_name,user_password):
    
    '''
    Function to create a user account 
  
    Args:
     name: function  to create user account   
    password: the password the user want for the account
        '''
        
    new_user = User(user_name,user_password)
    
    return new_user

def save_users(user):
    
    '''
    Function to save the user's details
    '''
    user.save_user()
    

def log_in(name,password):
    
    '''
    Function that enable the user to log-in into their credential account
    '''
    log_in = User.log_in(name, password)
    if log_in != False:
        return User.log_in(name, password)
    
    
def show_user():   
    '''
    This function show saved users

    '''
    return User.show_user()


def create_credential(credential_name,credential_password,user_account):

    '''
     Function to create credential
    '''

    new_credential = Credentials(credential_name,credential_password,user_account)
    return new_credential


def save_credential(credential):
    
    '''
   Function that saves credential
    
    Args:
        credential: credential that will be saved
        '''
    credential.save_credential()
    
    
def check_credentials(name):
        '''
        Function that check if the credential exist
        Args:
        name : the credential name
        '''

        return Credentials.check_credentials(name)

def show_credentials(password):
    
     '''
     Function that will show credential
    '''

     return Credentials.show_credentials(password)
 
 
def generate_password(name):
    '''
    It is a Function that generate a password for the user 
    Args:
        name : the name of the account
    '''
    password = Credentials.generate_password()

    return password

def main():
    '''
    Function run the password-locker
    '''

    print("Welcome to safe password-locker,Input your credentials to lock in")
    
    user_name = input()
    
    
    while True:
        '''
        loop will run in the whole application
        '''
        
        print('''Short_code:
            For log_in -li  \n
            For checking-credentials -cc \n
            For displaying-credentials - sc  \n
            For generating-password - gp \n
            For show-user - su  \n
            (For creating-credential - ct ''')
          
        short_code = input()
        
        if short_code == "li":
            
            
            '''
            create an locker account
            '''
            print("\n")
            print("New Credit Card Safe Account")
            print("-"*10)

            print("User name ...")
            user_name = input()

            print("Password ...")
            user_password = input()
           
           #creating a new account and saving it 
            
            save_users( create_user( user_name, user_password) )

            print("\n")
            print(f"{user_name} You have succefully created an account")
            print("\n")
            
        elif short_code == 'sc':
            '''
            show the credentials of the current users 
            '''
            
        if show_user():
            print("\n")
            print("List of current users")
            print("-"*10)
                
        for user in show_user():
                print(f"{user.user_name}")
                print("-"*10)
                    
        else:
            print("\n")
            print("This account has no users,Be the first user :)")
            print("\n")
            
            elif short_code == 'li':
                        '''
                        Logs in to access your account
                        '''
                        print("\n")
                        print("Log into your Password Account")
                        print("Enter the user name")
                        user_name = input()
 
            print("Enter the password")
            user_password = input()
            
            
            if log_in(user_name,user_password) == None:
                print("\n")
                print("Please provide your name and password \n aCreate an account if you don't have one")
                print("\n")

            else:

             log_in(user_name,user_password)
            print("\n")
            print(f'''{user_name} welcome to your Credentials\n
            Use these short codes to access your account and credentials''')
             
            while True:
             '''
             Loop to run functions after logging in
             '''
             print(''' 
             cd - create_credential \n
             sd - save credential \n
             ch - check credential \n
             ho - show credential \n
             gn  - generate password \n
              
              ''')

             
             short_code = input().lower()

             if short_code == 'cd':
                        '''
                        Creating a Credential
                        '''

                        print("\n")
                        print("Added  Credential")
                        print("-"*10)

                        print("Name of the credential ...")
                        credential_name = input()

                        print("Password of the credential ...")
                        credential_password = input()
            
            
                     
             elif short_code == 'cd':
                    '''
                    Creating new credentials 
                    '''

                    print("\n")
                    print("New Credential")
                    print("-"*10)

                    print("Name of the credential ...")
                    credential_name = input()

             if __name__ == '__main__':
                 main()             
            
