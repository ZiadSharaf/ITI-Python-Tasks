def Valid_Name(Name):
    if Name.strip()!="" and Name.isalpha():
        return True
    else:
        return False


def Valid_Email(Email):
    if '@' not in Email or '.' not in Email:
        return False

    parts_of_email=Email.split('@')
    first_part=parts_of_email[0]
    second_part=parts_of_email[1]

    if not first_part:
        return False
    if '.' not in second_part:
        return False
    
    domain_parts=second_part.split('.')    
    if not domain_parts[1]:
        return False

    return True
    
    