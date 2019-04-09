from super_functs import dead
from boss_room import boss_room

def riddle_room():
    print(""" Once you enter the room, you look around.
    It looks a lot like a forest, tall trees and various plants galore.
    You notice a troll napping on a tree stump in the middle of the room. 
    The door behind you slams shut and the troll wakes up.
    What do you do?""")
    
    while True:
        choice = input(" >")
        if "talk" in choice and "troll" in choice:
            print(""" "Welcome to my room of riddles!", says the troll. "I'll get straight to the point. I'm going to ask you
            a series of riddles. If you answer the first one correctly, I'll open the door from which you came.
            If you answer the second, I'll open the door that leads to the next room. If you feel you're not up to the task, 
            I might kill you right here! What do you say? Would you like to play?" """)
            
            while True:
                choice = input(" >")
                if choice.lower() == "yes":
                    first_riddle()
                elif choice.lower() == "no":
                    dead("The troll snaps his fingers, and you keel over in pain. Your last words were \" I don't feel so good\"")
                else:
                     print("It's a simple Yes or No answer!")
        else:
            print("You can't do that right now. Maybe talk to the troll?")
    

 
# def reset_riddle_room():
#     print("You're in the room of riddles. What now?")
#     choice = input(" >")

# riddle_room()

# first_riddle_right = False
# second_riddle_right = False

def first_riddle():
    print(""" "Let's begin! I have no mouth, but I still consume. Feed me well, and I will be strong. Get me to drink water, and I die.
    What am I?" """)
    choice = input(" >")
    if "fire" in choice.lower():
        print(""" "That's right, I'm fire! Talk to me when you want to try the next one. It won't be nearly as easy." """)
        second_riddle()
    else:
        dead('Nope, you fail the riddle. The troll keeps you prisoner forever.')

                    
def second_riddle():
    print(""" "You just received word that the princess is dead! In her room there's broken glass on the floor and a puddle of water. 
    Her window is open, and it's storming outside. The nightstand by her window is knocked over as well. If nobody was present when the princess
    died, then how did she die?" """)
    choice = input(" >")
    if "princess" in choice and "was" in choice and "fish" in choice:
        second_riddle_right = True
        print(""" "That's correct! The princess died because she was a fish! The wind from the storm broke her window
        and knocked down her nightstand, so her fish bowl broke and she suffocated as a result." *The door ahead opens*
        A shard of glass appears in your hand.
        "Good luck in the next room!" """)
        boss_room('pointy')
    else:
        dead('Nope, you fail the riddle. The troll keeps you prisoner forever.')