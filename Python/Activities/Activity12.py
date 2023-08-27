# Define function to calculate sum
def calculatesum(num):
    if num:
        # Recursive function call
        return num + calculatesum(num-1)
    else:
        return 0


# Call calculateSum() function
res = calculatesum(10)

# Print result
print(res)
