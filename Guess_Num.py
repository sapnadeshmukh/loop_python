index=1
while(index<=9):
    user=int(input("enter num"))

    a=range(1,9)
    if user in a:
        print("Well guessed!")
        break
    index=index+1