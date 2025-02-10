import re
from logger import user_logs

logger=user_logs()

def firstname_check(firstname):
    """Description : This method Checks if the first name starts with a capital letter and has at least 3 characters.
    
    Parameters : Single parameter named firstname 
    
    Return value:  String """
    
    if bool(re.match(r"^[A-Z][a-zA-Z]{2,}$", firstname)): #I have provided {2,}to make sure the last sequence gets repeated 2 or more times
        logger.info(f"User's firstname {firstname} was Vaild")
        return "Valid First Name"
    else:
        logger.error(f"Registration issue :User's firstname {firstname} was invalid.")
        return "Invalid First Name "
    
def last_check(lastname):
    """Description : This method Checks if the last name starts with a capital letter and has at least 3 characters.
    
    Parameters : Single parameter named lastname 
    
    Return value:  String """
    if bool(re.match(r"^[A-Z][a-zA-Z]{2,}$", lastname)): #I have provided {2,}to make sure the last sequence gets repeated 2 or more times
        logger.info(f"User's lastname {lastname} was Vaild")
        return "Valid Last Name"
    else:
        logger.error(f"Registration issue :User's lastname {lastname} was invalid.")
        return "Invalid Last Name "
    
def email_check(email):
    """Description : This method Checks if the user follows the rules for emails while registration.
    
       Parameters : Single parameter named email
    
       Return value:  String """
    
    if bool(re.match(r"^[a-zA-Z0-9_.*]+[a-zA-Z0-9_]*@[a-zA-Z.]+[a-zA-Z]+[a-zA-Z]$",email)):
        logger.info(f"User's email id {email} was Valid.")
        return "Valid Email Id"
    else:
        logger.error(f"Registration Issue: User's email id {email} was Invalid.")
        return "Invalid Email Id , Please enter a valid one"
        
    
    
def main():
    """Driver code to take user input and validate username."""       

    firstname = input("Enter First Name: ")
    lastname=input("Enter Last Name:")
    result_first = firstname_check(firstname)
    result_second = last_check(lastname)
    email=input("Enter the maid id :")
    
    print(result_first)
    print(result_second)
    print(email_check(email))
    

if __name__ == '__main__':
    main()