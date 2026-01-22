num = int(input("Enter a number: "))

digits = str(num)
power = len(digits)

total = 0
for d in digits:
    total += int(d) ** power

if total == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
