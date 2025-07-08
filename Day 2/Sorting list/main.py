from Sorting_list import Sorting_List_Aescending,Sorting_List_Descending
 
List=[]
for i in range(5):
    num=int(input(f"please enter number {i+1}: "))
    List.append(num)
    
Aescending_List=Sorting_List_Aescending(List)
Descending_List=Sorting_List_Descending(List)
    
print(f"Original list: {List}")    
print(f"Aescending list: {Aescending_List}")
print(f"Descending list: {Descending_List}")