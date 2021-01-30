row=int(input("enter number"))
column=int(input("enter number"))
i=0
small_list=[]
k=0
while (i<row):
    big_list=[]
    j=0
    while(j<column):
        k=j*i

        big_list.append(k)
        j=j+1

    i=i+1
    small_list.append(big_list)
print(small_list)


        