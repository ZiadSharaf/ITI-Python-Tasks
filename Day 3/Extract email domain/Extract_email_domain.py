def Emails_Extraction(Emails):
    Domains=list(map(lambda i:i.split('@')[1],Emails))
    return Domains
    