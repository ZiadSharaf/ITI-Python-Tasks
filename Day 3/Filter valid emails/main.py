from Filter_valid_emails import valid_email

Emails=["ACDV.COM","ali@gmail.com","sara@yahoo.com","mohamed@outlook.com","noha@iti.gov.eg","ssdaf@"]
Valid_Emails=list(filter(valid_email,Emails))
print(Valid_Emails)
