def Multiplication_Table(Number):
    Outer_List=[]
    for i in range(1,Number+1):
        Inner_List=[]
        for j in range(1,i+1):
            value=i*j
            Inner_List.append(value)
        Outer_List.append(Inner_List)
    return Outer_List
