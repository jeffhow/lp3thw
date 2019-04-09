from super_functs import dead
from boss_room import boss_room # Jacob

def bug_room():
    print("Bug Room")
    print("""
        There's a bunch of spiderwebs
        in front of the door , blocked by a giant spider! 
        There is a torch and a spear on the wall.
        """)

    while True:
        choice = input('> ')
        
        if "fight" in choice.lower():
            dead("You punch the spider in the face, but it eats your hand. You lose.")
            
        elif "burn" in choice.lower():
            print("Bye spider. Also, gross by the way.")
            print("Now the door is clear and you enter the boss room.")

            boss_room('fire')
            
        elif "spear" in choice.lower():
            print("You take the spear and throw it at the spider. The spider runs away!")
            print("Now the door is clear and you enter the boss room.")
            
            boss_room('pointy')
        else:
            print("I got no idea what that means.")
        
# def boss_room():
#     print("boss")
                
# def ogre_room():
#     print("ogre")
    