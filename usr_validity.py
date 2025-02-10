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

def main():
    """Driver code to take user input and validate username."""       

    firstname = input("Enter First Name: ")
    result_first = firstname_check(firstname)
    print(result_first)
    

if __name__ == '__main__':
    main()
