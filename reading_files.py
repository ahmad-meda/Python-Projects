from sys import argv

script, filename = argv

txt = open(filename)
print(f"hers's your {filename}:")
print(txt.read())


print("type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.readline())

#• close – Closes the file. Like File->Save.. in your editor.
#• read – Reads the contents of the file. You can assign the result to a variable.
#• readline – Reads just one line of a text file.
#• truncate – Empties the file. Watch out if you care about the file.
#• write('stuff') – Writes ”stuff” to the file.
#• seek(0) – Move the read/write location to the beginning of the file.

print(f"We're going to erase {filename}.")
print("If you dont want that hit crtl-C (^C).")
print("If you do want that hit Return")
input("?")

print("opening the file...")
target = open(filename, 'w')

print("Truncating the file goodbye!")
target.truncate()

print("now im going to ask you for three lines.")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("i'm going to write these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
