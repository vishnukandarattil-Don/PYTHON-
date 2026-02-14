# conditional statement
age = 18
Name = "Vishnu"
if (age > 25):
    print("you are eligible to vote")
elif (Name == "Vishnu"):
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

# if can use multiple conditions
# elif can use multiple conditions and only activate when the if condition is false
# else is used when all the conditions are false
# else is used only once and it should be the last condition
mark = input("enter your mark=")
mark = int(mark)
if mark >= 90:
    print("you got A grade")
elif mark >= 80 and mark < 90:
    print("you got B grade")
# elif can use multiple conditions and only activate when the if condition is false
elif mark >= 70 and mark < 80:
    print("you got C grade")
else:
    print("failed the exam")
