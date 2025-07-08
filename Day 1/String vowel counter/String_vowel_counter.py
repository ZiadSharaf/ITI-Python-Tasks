def Vowel_Counter(String):
    Vowels=['a','A','e','E','o','O','i','I','u','U']
    counter=0
    
    for i in String:
        if i in Vowels:
            counter+=1
    
    return counter
