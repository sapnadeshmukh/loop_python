new_list=[]
for index in range(100,401):
    num=str(index)
    if ((int(num[0])%2==0) and (int(num[1])%2==0) and (int(num[2])%2==0)):
        new_list.append(num)
print(new_list)

print(",".join(new_list))