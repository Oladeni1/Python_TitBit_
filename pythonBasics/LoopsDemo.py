
# For Loop
obj = [2, 3, 4, 5, 6, 9, 12]
for i in obj:
    print(i)
    print(i*2)  # Print multiple of 2

print("====End of for loop1====")

# List of numbers 1 + 2 + 3 + 4 + 5
# range(i,b) -> i to b-1
for b in range(1, 6):
    print(b)  # prints 1 to 5

print("====End of for number listing loop====")

# Sum of numbers 1 + 2 + 3 + 4 + 5 = 15
addition = 0
for y in range(1, 6):
    addition = addition + y
print(addition)  # prints 15
