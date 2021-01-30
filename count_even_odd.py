numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count_even=0
count_odd=0
index=0
while(index<len(numbers)):
    if (numbers[index]%2==0):
        count_even=count_even+1
    else:
        count_odd=count_odd+1
    index=index+1
print("count_even:",count_even)
print("count_odd:" ,count_odd)
