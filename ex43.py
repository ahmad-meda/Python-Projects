from sys import argv
script, input_file = argv
my_story = open(input_file)
print(my_story.read())
my_story.close()
