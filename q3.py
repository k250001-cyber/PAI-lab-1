numbers = []
n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    val = int(input("Enter number: "))
    numbers.append(val)

even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count = even_count + 1

print("Count of even numbers:", even_count)
