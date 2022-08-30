i = 0
numbers = []
while i < 6:
    print(f"at the top i is {i}")
    numbers.append(i)
    i += 1
    print("numbers now:", numbers)
    print(f"At the bottom is {i}")
print("the numbers")
for num in numbers:
  print(num)
