user1=int(input("enter num1="))
user2=int(input("enter num2="))
user3=int(input("enter num3="))
if (user1<user3 and user1<user2):
    print(user1)
elif (user2<user1 and user2<user3):
    print(user2)
else:
    print(user3)