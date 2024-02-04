password = "Adminmmm1"

def check_password(password):
    if len(password) < 8 or len(password) > 20:
        return False
    
    smallletter = 0 
    capitalletter = 0
    digithave = 0

    for letter in password:
        if letter.islower():
            smallletter = 1
        if letter.isupper():
            capitalletter = 1 
        if letter.isdigit():
            digithave = 1
        
    if capitalletter == 0 or smallletter == 0 or digithave == 0:
        return False
    
    return True
    



if check_password(password):
    print("Strong Password")
else:
    print("Bad Password")