# Array
mark1 = 92.4
mark2 = 95.6
mark3 = 98.5
# for a list of marks we can use an array using [use, se, use]
marks = [92.4, 95.6, 98.5]
print(marks)
print(marks[1])
print(len(marks))
# Strings are immutable but lists are mutable
student = ["Vishnu", 18, "Bangalore"]  # this is a list of student details
print(student)
student[1] = 19  # mutable means we can change the value of the list
print(student)
student[0] = "Vikki"
print(student)

# list slicing
# similar to string slicing
print(student[0:2])  # 0 to 1
print(student[0:3])  # 0 to 2
print(student[0:3:2])  # 0 to 2 with step 2
print(student[1:])  # from 1 to end
print(student[-1])  # last element
print(student[-3:-1])  # from -3 to -2

# list methods
list = [1, 2, 3, 4, 5]
list.append(6)  # adds an element to the end of the list
print(list)
list.sort()
print(list)
list.reverse()  # reverses the list
print(list)
list.insert(2, 10)  # inserts 10 at index 2
print(list)


# TUPLES
# tuples are immutable
tuple1 = (1+2, 2, 3, 4, 5)
# use parenthesis for tuples
print(tuple1)
print(type(tuple1))
# task
# WAP to ask the user enter 3 actor name and store in a list
actor1 = input("enter actor 1 name=")
actor2 = input("enter actor 2 name=")
actor3 = input("enter actor 3 name=")
actor = [actor1, actor2, actor3]
print(actor)

# task 2
# WAP to check if a list contains a palindrome of elements
userlist = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(userlist)
plaindrome = userlist.copy()
plaindrome.reverse()
print(plaindrome)
if userlist == plaindrome:
    print("the list is a palindrome")
else:
    print("the list is not a palindrome")
