numbers = []
n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    val = float(input("Enter number: "))
    numbers.append(val)

total = 0
for num in numbers:
    total = total + num

print("Sum of elements:", total)
