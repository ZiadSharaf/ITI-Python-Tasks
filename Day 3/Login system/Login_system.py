def Validation(Name,Data_Base):
    for i in Data_Base:
        if i["Name"]==Name:
            Password=input("please enter your password: ")
            if i["Pass"]==Password:
                print("Done!")
                break
            else:
                print("Incorrect password")
                break
        else:
            continue
    else:
        print("Name not found")
        