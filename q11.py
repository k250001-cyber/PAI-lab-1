english = float(input("Enter English marks (out of 100): "))
computer = float(input("Enter Computer marks (out of 100): "))
science = float(input("Enter Science marks (out of 100): "))

marks = {}
marks["English"] = english
marks["Computer"] = computer
marks["Science"] = science

total = marks["English"] + marks["Computer"] + marks["Science"]
average = total / 3
percentage = (total / 300) * 100

print("Average:", average)
print("Percentage:", percentage)
