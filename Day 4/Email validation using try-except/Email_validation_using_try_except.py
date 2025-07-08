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



