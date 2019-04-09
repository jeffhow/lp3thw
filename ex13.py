from sys import argv
# argv allows you to define arguments to pass to the script when run.
script, first, second, third = argv

print("THe script is called:", script)
print("Your first var is:", first)
print("Your second var is:", second)
print("Your third var is:", third)
fourth = input("Give me another: ")
print("Your fourth var is:", fourth)