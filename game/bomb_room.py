from super_functs import dead
from boss_room import boss_room

def bomb_room():
  print("There is a bomb here,")
  print("It is sensetive so it will explode very easily if not careful.")
  print("There are 2 wires to pull, one will disable the bomb, but the other one will instantly explode!")
  print("Which one do you choose?")
  bomb_detonated = False
  
  while True:
      choice = input('> ')
      
      if choice == "Wire 1" and bomb_detonated:
          dead("That was the wrong wire.")
      elif choice == "Wire 2" and not bomb_detonated:
          print("You've picked the right wire carefully.")
          print("You now have a bomb as an item!")
          print("Proceed to the final room.")
          boss_room('bomb')
      elif choice == "Wire 2" and bomb_detonated:
          dead("You pulled it too hard.")
      else:
          dead("Are to going to type an actual choice or just stand there, because there's a standing fee.")
          