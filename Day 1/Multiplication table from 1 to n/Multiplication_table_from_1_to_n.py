def Multiplication_Table(Number):
    print("\nMultiplication Table:")
    
    for i in range(1,Number+1):
        for j in range(1,i+1):
            print(f" {i} * {j} = {j*i}")
        print("")

