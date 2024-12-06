#Grade student based on marks

marks=int(input("Enter the marks of students:"))

if(marks>=90):
    grade="A"
elif(96>marks>=80):
    grade="B"
elif(80>marks>=70):
    grade="C"
elif(marks<70):
    grade="D"

print("The grade of student is:",grade)
