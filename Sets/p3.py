#WAP to enter the marks of 3 subjects from the user and store them in a dicitionary. Start with an empty dicitonary and add one by one. Use subject name as key and marks as value.
marks={}

s=int(input("Enter phy:"))
marks.update({"phy":s})

s=int(input("Enter chem:"))
marks.update({"chem":s})

s=int(input("Enter math:"))
marks.update({"math":s})

print(marks)