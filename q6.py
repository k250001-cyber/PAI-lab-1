physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))
maths = float(input("Enter Maths marks: "))

marks = {}
marks["Physics"] = physics
marks["Chemistry"] = chemistry
marks["Maths"] = maths

total = marks["Physics"] + marks["Chemistry"] + marks["Maths"]
average = total / 3

highest_subject = "Physics"
highest_mark = marks["Physics"]

if marks["Chemistry"] > highest_mark:
    highest_subject = "Chemistry"
    highest_mark = marks["Chemistry"]

if marks["Maths"] > highest_mark:
    highest_subject = "Maths"

print("Average marks:", average)
print("Highest marks in:", highest_subject)
