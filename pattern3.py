n = int(input('Enter number of rows : '))
 
k = 1
i = 1
while i <= n :
    j = 1
    while j <= i:
        print(k, end = " ")
        j =j+ 1
        k =k+1 
    print()
    i += 1