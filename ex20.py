from sys import argv
script, input_file = argv
def print_all(f):
    print(f.read())
def rewind(f):
    f.seek(0)
def print_a_line(line_count, f):
    print(line_count, f.readline())
current_file = open(input_file)

print("first let's print the whole file:\n")
print_all(current_file)
print("Now lets rewind, kind of like a tape")
rewind(current_file)
#you have to think about files as if they’re tapes.
#You read a file (play the tape), write to a file (record to the tape), and the read/write head moves to that spot.
#If you want to back up and listen to what you just recorded, you have to seek to it or rewind it.
print("lets print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
