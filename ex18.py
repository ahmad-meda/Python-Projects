def print_two(*args):
    arg1, arg2 =args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin'.")

def my_first_try(*args):
    arg1, arg2, arg3 = args
    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}")

print_two("ahmad","meda")
print_two_again("ahmad","meda")
print_one("First!")
print_none()
my_first_try("ahmad","meda","Abdurrahman")
