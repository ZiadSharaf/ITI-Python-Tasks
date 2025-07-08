from Email_validation_using_try_except import valid_email

Number_Of_Attempts=0

while Number_Of_Attempts<5:
    try:
        Email=input("Enter your email: ")
        if valid_email(Email):
            print("Valid email.")
            break
        else:
            raise ValueError("Invalid email, Please try again!")
    except ValueError:
        Number_Of_Attempts+=1
        if Number_Of_Attempts<5:
            print("Invalid email, Please try again!")
else:
    raise("Access denied!")
