# strings are immutable

str1 = "this is a string\t"  # /t is used for tab space
str2 = "this is Vikki world"
str3 = "\n Vishnu is the  real Vikki"  # \n is used for new line
print(str1, str2, str3)
print(str1+str2 + str3)
print(len(str1))

# indexing

print(str1[2])

# slicing

print(str1[0:4])  # 0 to 3
print(str1[0:9:2])  # 0 to 9 with step 2
print(str1[5:])  # from 5 to end

# negative indexing

print(str1[-1])  # last character
print(str1[-5:-1])  # from -5 to -2

# string functions
print(str1.upper())  # converts to uppercase
print(str1.endswith("ring\t"))
ch = str1.capitalize()  # capitalizes the first letter
print(ch)
ch1 = str1.replace("t", "0")  # replaces 'this' with 'that'
print(ch1)

# practice
name = input("enter your name=")
print(len(name))
name = print(input("enter your name="))
print(len(name))
