from String_vowel_counter import Vowel_Counter

String=input("Please enter a string: ")
Counter=Vowel_Counter(String)

if Counter==0:
    print(f"There are no vowels in the string '{String}'.")
else:
    print(f"Number of vowels in '{String}' = {Counter}")
