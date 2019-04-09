from sys import exit
from super_functs import dead

def boss_room(item):
    print("This room is cold and dim. Smells like rotten meat and dead bodies. You see a dead knight in front of your feet with an axe jamed into his ribs.")
    print("The door closes behind you and locks. You look around and see a 4 leged and 4 armed 39 feet tall Pop-Corn machine! With a mouth the size of a bear, with curnals for eyes.")
    
    boss = True
    axe = False
    stabbed = False
    
    # ignis = True
    # spear = True
    # bomb = True
    # spark = True
    # sword = True
    # glasses = True
    # fire = True
 
    while boss:
        choice = input("> ")
        
        if "pick up axe" in choice:
            print("taken")
            axe = True
            
        if "attack" in choice and item=='pointy':
            print("You swing the axe and chop of one of its arms. It kicks you to the wall with one of its legs. It takes your axe and swallows it. ")
            axe = False

        elif "ignis" in choice and item=='fire': 
            print("You throw the fire ball at the monster's eye. It's eye pops into a giant peice of popcorn.")
            print("You no longer know the ignis spell")
            item = False
            choice = input(">")
            
        elif "ignis" in choice and item=='fire':
            print(f"You throw the fire ball at the spot were the {item} had struck. The fire burns the monster's open wound, the monster screams in pain. The fire spreads though the monster's organs and...")
            print("The monster explodes into giant popcorn peices and is now dead.")
            print("Congrats you WIN. Sadly you cant get out. Now you are the boss of this room.")
            boss = False

        elif "spark" in choice and item=='spark':
            print("You electricute the monster but its not dead. You only stuned it for about 5 secounds.")
            print("You no longer know the spark spell.")
            item = False
            choice = input(">")
         
        elif "sword" in choice or "spear" in choice and item=='pointy':
            print("You charge the monster with your spear, dodging each one of its arms and legs. You slide under it's belly and as you slide under you throw the spear into its belly.")
            print("The monster screams in pain and pulls out the spear and throws it at you. You some how dodge it. The spear crashes into the floor breaking it, and leaving a giant whole.")
            print("You look in the hole and you see a giant pit of lava at the bottom of the whole.")
            item = False
            choice = input(">")
            
        elif "use bomb" in choice and item=='bomb':
            print("You throw the bomb at the monster with your perfect timing skills. Th bomb explodes in its face knocking it backwards into the pit of lava.")
            print("The monster falls into the lava and is now dead. You start to walk away. But as you are walking away you hear the pit of lava start to rumble.")
            print("You look back towards the big whole and hear a loud BOOM. Pop corn starts to fly out the whole and land on the floor. Congrats you WIN sadly you cant get out")
            bomb = False
            boss = False
            
        else:
            print("i dont know what that means")
            choice = input("> ")
            
    dead("You are stuck here. Now you are the boss. Moral of this story: Don't just go into random castles without an invitation.")          
# Boss_room()