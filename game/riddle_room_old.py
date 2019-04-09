from super_functs import dead

def riddle_room():
    
    print(""" Once you enter the room, you look around.
    It looks a lot like a forest, tall trees and various plants galore.
    You notice a troll napping on a tree stump in the middle of the room. 
    The door behind you slams shut and the troll wakes up.
    """)
    
    # First Riddle
    print(""" 
        "Let's begin! I have no mouth, but I still consume. 
        Feed me well, and I will be strong. 
        Get me to drink water, and I die.
        What am I?" 
        """)
        
    choice = input(" >")

    if "fire" not in choice.lower():
        print("That's wrong! It's FIRE!!!")
        die("The troll blasts you with fire and you lose.")
    else:
        print(""" 
            "That's right, I'm fire! 
            Talk to me when you want to try the next one.
            It won't be nearly as easy." 
            """)
            
    # Second Riddle               
    print(""" 
        "You just received word that the princess is dead! 
        In her room there's broken glass on the floor and a puddle of water. 
        Her window is open, and it's storming outside. 
        The nightstand by her window is knocked over as well. 
        If nobody was present when the princess
        died, then how did she die?" 
        """)
    
    choice = input(" >")
    
    if ("princess", "was", "fish") in choice.lower():
        print("""
            "That's correct! The princess died because she was a fish! 
            The wind from the storm broke her window
            and knocked down her nightstand, so her fish bowl broke 
            and she suffocated as a result!" 
            *The door ahead opens*
            "Good luck in the next room!" 
            """)
        boss_room()
    else:
        print("No! She was a fish!!")
        die("The troll turns into a giant fish and swallows you whole. You lose.")
