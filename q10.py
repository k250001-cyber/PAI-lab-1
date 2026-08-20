numbers = []
n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    val = float(input("Enter number: "))
    numbers.append(val)

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)
