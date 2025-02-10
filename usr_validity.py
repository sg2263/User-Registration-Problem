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
    
def contact_check(ph_no):
    """Description : This method Checks if the user follows the correct phone number format while registration.
    
       Parameters : Single parameter named phone number 
    
       Return value:  String """
        
    
    if bool(re.match(r"^[0-9]{2} [0-9]{10}$",ph_no)):
        logger.info(f"User's contact {ph_no} was Valid.")
        return "Valid Contact Detail"
    else:
        logger.error(f"Registration Issue: User's contact {ph_no} was Invalid.")
        return "Invalid Contact details"
    
def password_rule1(password):
    """Description : This method Checks for the rule 1 defined under usecase 5.This checks if the password entered by the user has atleast 8 chracters.
    
       Parameters : Single parameter user password
    
       Return value:  boolean value True if it matches the search pattern ,else False."""
        
    
    if bool(re.match(r".{8,}",password)):
        logger.info(f"User's password passed Rule 1.")
        return True
    else:
        logger.error(f"Registration Issue: User's password was Invalid [Didn't Pass Rule 1].")
        return False
    
        
    
    
def main():
    """Driver code to take user input and validate username."""       

    # firstname = input("Enter First Name: ")
    # lastname=input("Enter Last Name:")
    # result_first = firstname_check(firstname)
    # result_second = last_check(lastname)
    # email=input("Enter the maid id :")
    # ph_no=input("Enter the phone number in correct format:")
    
    # print(result_first)
    # print(result_second)
    # print(email_check(email))
    # print(contact_check(ph_no))
    password=input("Enter the user password: ")
    if password_rule1(password):
        print("Passes rule 1.")
    else:
        print("Failed Rule 1")
        
    

if __name__ == '__main__':
    main()