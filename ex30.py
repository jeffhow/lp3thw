people, cars, trucks = 30, 40, 15

if cars > people: # 40 > 30 ? True
    print("We should take cars.") # This one
elif cars < people:
    print("we should not take cars.")
else:
    print("We can't decide.")
    
if trucks > cars: # 15 > 40 ? False
    print("Too many trucks.")
elif trucks < cars: # 15 < 40 ? True
    print("Maybe we take trucks.") # This one
else:
    print("No decision.")
    
if people > trucks: # 30 > 15 ? True
    print("Alright, take trucks.") # This one
else:
    print("Fine, stay home.")
    
# Take cars, maybe trucks, take trucks.