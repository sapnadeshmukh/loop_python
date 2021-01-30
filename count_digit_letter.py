string = input("Input a string")
digit=0
letter=0
for index in string:
    if index.isdigit():
        digit=digit+1
    elif index.isalpha():
        letter=letter+1
    else:
        pass
print("Letters", letter)
print("Digits", digit)