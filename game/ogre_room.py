from bug_room import bug_room # Room 4 Jose
from magic_room import magic_room

# Ryan, room 1

# def magic_room():
#     print("magic_room")
    
# def bug_room():
#     print("bug_room")

def ogre_room():
    print("This room has an 8 foot ogre blocking the exit.")
    print("The ogre does the roar")
    print("The ogre turns around")
    print("""Do you want to sneak around it or hit it in the back of the head?""")
    
    sword = False

    while True:
        
        choice = input("> ")
        
        if "sneak" in choice:
            print("You sneak around the ogre. and find a sword near the next exit")
            print("There is a sword and a door, what do you do?")
            choose_door_or_sword()
            
            
        elif "hit" in choice:
            print("You feel like you're Chuck Norris and punch the ogre in the back of the head.")
            print("This causes the ogre to fall on the ground and fall into a coma")
            print("You spot a sword near the next exit.")
            choose_door_or_sword()
        
        else:
            print("I got no idea what that means.")
            
def choose_door_or_sword():
    while True:
        choice = input("> ")
        
        if "take" in choice.lower():
            sword = True
            print("You took the sword but you can't fight because you don't know how to wield a sword.")
            print("To learn, remember these words, \"Gladius ad Deum\"")
            print("You feel all tingly and are suddenly in another room")
            magic_room()
            
        elif "door" in choice.lower():
            print("You go through the door.")
            bug_room()
            
        else:
            print("I got no idea what that means.")
            
            
# ogre_room()