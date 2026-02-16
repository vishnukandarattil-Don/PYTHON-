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
list.append(4)  # adds an element to the end of the list
print(list)
list.sort()
print(list)
list.reverse()  # reverses the list
print(list)
list.reverse()
print(list)
list.insert(2, 10)  # inserts 10 at index 2
print(list)
