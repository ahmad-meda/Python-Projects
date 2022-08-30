ten_things = "Apples oranges Crows Telephone Light Sugar"
print("Wait,there are no 10 things in that list.lets fix that.")
stuff = ten_things.split(' ')
more_stuff = ["day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding:", next_one)
    stuff.append(next_one)
    print(f"There are  {len(stuff)} items now.")
print("There we go:", stuff)
print("Lets do some things with stuff")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))#Apples oranges Crows Telephone Light Sugar Boy Girl Banana <---(result)
print('#'.join(stuff[3:5]))
