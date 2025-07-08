def Mario_Pyramid_List():
    List=[" "," "," "," "," "]
    
    for i in range(5):
        List.append("*")
        List.pop(0)
        print(List)
    