the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f"This is count {number}")
for fruit in fruits:
    print(f"A fruit of type: {fruit}")
for x in change:
    print(f"I got {x}")

elements = []
for i in range(0,6):
    print(f"Adding {i} to the list")
    elements.append(i)
for x in elements:
    print(f"Element was: {x}")
