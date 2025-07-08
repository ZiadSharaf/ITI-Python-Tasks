import csv
def valid_email(Email):
    if '@' not in Email or '.' not in Email:
        return False

    Parts_Of_Email=Email.split('@')
    First_Part=Parts_Of_Email[0]
    Second_Part=Parts_Of_Email[1]

    if not First_Part:
        return False
    if '.' not in Second_Part:
        return False
    
    Domain_Parts=Second_Part.split('.')    
    if not Domain_Parts[1]:
        return False

    return True


Emails=[]
with open("customer_data.csv", "r", newline="") as file:
    reader=csv.DictReader(file)
    for i in reader:
        Emails.append(i["Email"])

Validated_Emails=list(filter(valid_email,Emails))

Domains=list(map(lambda i:i.split('@')[1],Validated_Emails))

Domain_Names=list(map(lambda i:i.split('.')[0],Domains))

Domain_Names=set(Domain_Names)

print(f"Domain Names: {Domain_Names}")