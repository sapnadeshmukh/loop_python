first_side=int(input("enter number"))
second_side=int(input("enter number"))
third_side=int(input("enter number"))		
if (first_side==second_side==third_side):
    print("equilateral triangle")
elif(first_side==second_side or second_side==third_side or third_side==first_side):
    print("isosceles triangle ")
else:
    print("scalene triangle")