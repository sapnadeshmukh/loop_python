numbers=[4,5,9,56,32,12,67,98,45,23,981,123,435,654,1134,1212]
i=0
max_num=0
second_num=0
while(i<len(numbers)):
    if numbers[i]>max_num:
        max_num=numbers[i]
    i=i+1
    j=0
    while (j<len(numbers)):
        if (max_num>numbers[j] and  second_num<numbers[j]):
            second_num=numbers[j]
        j=j+1
print(max_num)
print(second_num)



