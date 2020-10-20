def fibino(n):
    a,b,sum,count = 0,1,0,1
    print("Fibonacci Series: ", end = " ")
    while(count <= n):
        print(sum, end = " ")
        count += 1
        a,b = b,sum
        sum = a + b

n = int(input("Enter the value of 'n': "))
fibino(n)