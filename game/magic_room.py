from super_functs import dead
from boss_room import boss_room

def magic_room():
    print("Magic Room")
    print("As soon as you materialize into the room you were greeted with a flying book almost hitting you in the face.")
    print("The room was covered with shelves filled with books which you assume are spell books.'Greetings!' a voice said.")
    print("You scanned the room and notice an old man sitting in a wooden chair reading a book, in front of him there was a table with three books on them.")
    print("One books says 'Ignis' (which means 'Fire' in Latin), another books says 'Scintillam' (which means 'Spark' in Latin),\nhe final book says 'Gladius ad Deum' (which means 'God of the Sword' in Latin).")
    print("'You're only allowed to learn book for that spell,' said the old man 'be careful what you chose!'\n What book will you chose?""")
    
    while True:
        choice = input('> ')
        
        if "fire" in choice.lower() or "ignis" in choice.lower():
            
            print("'I see that you like burning things down.'")
            print("You have learned Ignis!")
            proceed('fire')
            
        elif "spark" in choice.lower() or "scintillam" in choice.lower():
            
            print("'That will SHOCK most people, get it?'")
            print("You have learned Scintillam!")
            proceed('spark')
            
        elif "god of the sword" in choice.lower() or "gladius ad deum" in choice.lower():
            
            print("Why would want that spell, all it does is make you able to use a power magical sword... oh well.")
            print("You have learned Gladius ad Deum!")
            proceed('pointy')
        else:
            
            print("You have to pick a book.")

def proceed(spell):      
    print("'Hope you picked the right one...' says the old man")
    print("smoke cam into the room blinding you.")
    print("As soon as the smoked cleared all that was left was empty shelves and an empty table.")
    print("The old man vanished including the books.")
    print("Behind where the old man was sitting there's a strange door that reads 'Boss Room'")
    print("You took a deep breath and enter the Boss Room.")
    boss_room(spell)
