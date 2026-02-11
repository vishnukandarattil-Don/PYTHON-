print("hello I Vishnu K", ", this is my code on finding area of a circle",
      "and area of a rectangle")
# area of a circle
radius = int(input("enter the radius of the circle"))
area = print("Area=", 3.14*radius*radius, "sq units", 3.14*radius**2)
length = int(input(" enter the length of the rectangle="))
breadth = int(input("enter the breadth of the rectangle="))
Area = print("Area of rectange=", length*breadth, "sq units")
name = input("enter your name=")

# Uage of type function
print(type(radius))
print(type(length))
print(type(breadth))
print(type(name))


# Arithmetic operators
a = 10
b = 20
sum = a+b
print("the sum of a and b is=", sum)
difference = a-b
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)


type conversion
c, d = 5, int("20")
e, f = str(c), str(d)
print("the value of e and f is=", c, d)
print(c+d)

# WAP to input 2 floats and print their average
g = float(input("enter the first number="))
h = float(input("enter the second number="))
average = (g+h)/2
print("the average of the two numbers is=", average)
