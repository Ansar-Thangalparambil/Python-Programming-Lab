#Lambda to find the area of square rectangle & triangle

a=int(input("Enter the side of the square \n"))
area = lambda b:b*b
print("area of square",area(a))

a=int(input("Enter the length of the rectangle"))
b=int(input("Enter the breadth of the rectangle"))
area=lambda l,b:l*b
print("Area of the rectangle is",area(a,b))

a=int(input("Enter the height of the triangle \n"))
b=int(input("Enter the breadth of the triangle \n"))
area=lambda h,b:h*b
print("Area of triangle is",area(a,b))
