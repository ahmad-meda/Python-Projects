people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("we should not take the cars.")
else:
    print("We cant decide.")

if trucks > cars:
    print("Thats's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("we still cant decide.")

if people > trucks:
    print("Alright, lets just take the trucks.")
else:
    print("Fine,lets stay at home then.")
    
