from super_functs import dead

from riddle_room import riddle_room
from bomb_room import bomb_room

# def castle_room():
#     print("game over")
    
def choice_room():
    print(""" 
    You are suddenly hit by an intense and godly light.
    then with no warning it is consumed by the black.
    feet, body, hands, head, eyes, mind all was black. 
    in what semmed like the longest second, small, soft, lights  flicked illuminated the black room.
    two floating orbs appear in front of you.
    
    a soft voice wispers "your choice to make"
    
    """)
    
    while True:
        choice = input("> ")
    
        if(choice == "choice"):
            choice_room_man()
        else:
            dead("You chose wrong. You lose")

def choice_room_man():
        
    print("""
    the walls begin to callapes ligh, matter and mind all fold.
    compersing in on its self 
    a burst of particles, matter begins to take shape
    you body forms and the your mind
    
    a kirby shaped man appearse. 
    the wisper you heard shapes form
                              _
                           _ooOoo_
                          o8888888o
                          88" . "88
                          (| -_- |)
                          O\  =  /O
                       ____/`---'\____
                     .'  \|\|     |//  `.
                    /  \|\|||  :  |||//  \
                   /  _||||| -:- |||||_  \
                   |   | \|\  -  /'| |   |
                   | \_|  `\`---'//  |_/ |
                   \  .-\__ `-. -'__/-.  /
                 ___`. .'  /--.--\  `. .'___
              ."" '<  `.___\_<|>_/___.' _> /"".
             | | :  `- \`. ;`. _/; .'/ /  .' ; |
             \  \ `-.   \_\_`. _.'_/_/  -' _.' /
   ===========`-.`___`-.__\ \___  /__.-'_.'_.-'================
    
    """)
    print('" yes or no are you a jurney man", he ask')
    
    
    while True:
        choice = input("> ")
    
        if(choice == "yes"):
            print("yes, you say.")
            
            bomb_room()
        
        elif(choice == "no"):
            print("no, you say.")  
            
            bomb_room()
            
        
        else:
            print("i am a man of yes or no")
            print(f'but you a man of words say "{choice}"')
            print("okay")
            print("""
            the room begims to spin.
            fast and faster it goes
            you are floating with mysteriuos man
        
            he screams "IM KILASKHIS FATHER OF THE ELDER GOOS, SAGE OF INFINATE PATHS, YOU HAVE NADE YOUR CHOICE"
            """)
            
            riddle_room()
