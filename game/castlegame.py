from super_functs import dead
from ogre_room import ogre_room, choose_door_or_sword # Room 1 Ryan
from choice_room import choice_room, choice_room_man # Room 2 Mac


def start():
    print('''
        Beyond the Castle
                                       /\
                                      /`:\
                                     /`'`:\
                                    /`'`'`:\
                                   /`'`'`'`:\
                                  /`'`'`'`'`:\
                                   |`'`'`'`:|
     _ _  _  _  _                  |] ,-.  :|_  _  _  _
    ||| || || || |                 |  |_| ||| || || || |
    |`' `' `' `'.|                 | _'=' |`' `' `' `'.|
    :          .:;                 |'-'   :          .:;
     \-..____..:/  _  _  _  _  _  _| _  _'-\-..____..:/
      :--------:_,' || || || || || || || `.::--------:
      |]     .:|:.  `' `'_`' `' `' `' `'    | '-'  .:|
      |  ,-. .[|:._     '-' ____     ___    |   ,-.'-|
      |  | | .:|'--'_     ,'____`.  '---'   |   | |.:|
      |  |_| .:|:.'--' ()/,| |`|`.\()   __  |   |_|.:|
      |  '=' .:|:.     |::_|_|_|\|::   '--' |  _'='.:|
      | __   .:|:.     ;||-,-,-,-,|;        | '--' .:|
      |'--'  .:|:. _  ; ||       |:|        |      .:|
      |      .:|:.'-':  ||       |;|     _  |]     _:|
      |      '-|:.   ;  ||       :||    '-' |     '--|
      |  _   .:|].  ;   ||       ;||]       |   _  .:|
      | '-'  .:|:. :   [||      ;|||        |  '-' .:|
  ,', ;._____.::-- ;---->'-,--,:-'<'--------;._____.::.`.
 ((  (          )_;___,' ,' ,  ; //________(          ) ))
  `. _`--------' : -,' ' , ' '; //-       _ `--------' ,'
       __  .--'  ;,' ,'  ,  ': //    -.._    __  _.-  -
   `-   --    _ ;',' ,'  ,' ,;/_  -.       ---    _,
       _,.   /-:,_,_,_,_,_,_(/:-\   ,     ,.    _
     -'   `-'--'-'-'-'-'-'-'-''--'-' `-'`'  `'`' `
    ''')
    print("You find an abandoned castle in the woods.")
    print("Seeking your fortune, you decide to investigate.")
    print("As you enter the castle, a tree falls, blocking your exit.")
    print("When the dust settles, ")
    castle_room()

def castle_room():
    print("you see that you are an empty stone room.")
    print("There is a door on the left and a door on the right.")
    print("Choose a door, left or right?")
    
    while True:
        choice = input('> ')
        
        if "left" in choice.lower():
            print("You go through the left door.")
            ogre_room() # Room 1
        elif "right" in choice.lower():
            print("You go through the right door.")
            choice_room()
        else:
            print("You can only choose 'left' or 'right'")

# def ogre_room():
#     print('ogre room')
#     exit(0)

# def choice_room():
#     print('choice room')
#     exit(0)


    
start()