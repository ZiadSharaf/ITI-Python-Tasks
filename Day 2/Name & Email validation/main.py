from Name_Email_validation import Valid_Name,Valid_Email
    
Name=input("Please enter you name: ") 
if (Valid_Name(Name)):
    Email=input("Please enter your email: ")
    
    if (Valid_Email(Email)):
        print("\nYour data: ")
        print(f"Name: {Name}")
        print(f"Email: {Email}")
    else:
        print("Invalid email")
else:
    print("invalid name! Your name must contain only letters and no spaces.")