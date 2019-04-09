ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one )
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now")
    
print("There we go: ",stuff)

print("Let's do some things with stuff.")

# Prints index 1
print(stuff[1])

# Prints last item in list
print(stuff[-1]) # Whoa! fancy

# prints last item and removes it from list
print(stuff.pop()) 

# prints list values with spaces in between 
print(' '.join(stuff)) # What? Cool!

# prints index 3 and 5 with # in between
print('#'.join(stuff[3:5])) # Stuper Stellar!