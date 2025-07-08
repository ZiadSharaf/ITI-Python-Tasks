def find_letter_i_index(String):
    Index=[]
    if 'i' in String:
        for i in range(len(String)):
            if String[i]=='i':
                Index.append(i)
        print(f"The indexes of the letter 'i' in the string '{String}' = {Index}.")
    else:
        print(f"There is no letter 'i' in the string '{String}'.")
        

