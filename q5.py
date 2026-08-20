numbers = []
n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    val = float(input("Enter number: "))
    numbers.append(val)

limit = float(input("Enter threshold number: "))

filtered_numbers = []
for num in numbers:
    if num >= limit:
        filtered_numbers.append(num)

print("Filtered list:", filtered_numbers)
