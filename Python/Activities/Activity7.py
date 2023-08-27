numbers = list(input("Enter a sequence of comma separated numbers to find the sum: ") .split(","))
sums = 0
for number in numbers:
    sums += int(number)

print(sums)
