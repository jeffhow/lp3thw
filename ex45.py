import random
from sys import exit
from time import sleep

class Villian(object):
    hp=0
    attk=0
    name=''
    
    def __init__(self):
        self.hp = random.randint(1,20)
        self.attk = random.randint(1,5)
        names = ['orc', 'goblin', 'kobold']
        self.name = names[random.randint(0,2)]
    
    def description(self):
        print(f'The {self.name} has {self.hp} health and a +{self.attk} attack bonus')
    
    def attack(self):
        hit = random.randint(1,5)+self.attk
        if( hit > 4 ):
            print(f'The {self.name} hits you. you take {hit} points of damage.')
            return hit
        else:
            print(f'The {self.name} misses you.')
            return 0
        

class Game(object):
    hp=0
    attk=0
    name=''
    wins=0
    
    def __init__(self):
        self.hp=random.randint(15,40)
        self.attk = random.randint(1,5)
        self.name = input('Enter a name > ')
    
    def attack(self):
        hit = random.randint(1,5)+self.attk
        if( hit > 2 ):
            print(f'You hit the {self.villian.name}. It takes {hit} points of damage.')
            return hit
        else:
            print(f'You miss the {self.villian.name}.')
            return 0
    
    def description(self):
        print(f'{self.name} has {self.hp} health and a +{self.attk} attack bonus.')
    
    def start(self):
        print('Welcome to my game.')
        sleep(0.5)
        
        difficulty = input('Choose a difficulty level (1-3): > ')
        
        while(self.wins<int(difficulty)):
            self.villian=Villian()
            print(f'A {self.villian.name} appears!')
            sleep(0.5)
            self.villian.description()

            while(self.villian.hp>0):
                sleep(0.5)
                print(f'The {self.villian.name} attacks you!')
                sleep(0.5)
                self.hp -= self.villian.attack()
                self.description()
                sleep(0.5)
                
                if(self.hp>0):
                    action = input('Will you [A]ttack or [R]un? > ')
                    if 'A' in action:
                        self.villian.hp-=self.attack()
                        self.villian.description()
                        sleep(0.5)
                        input('Press any key to continue > ')
                    else:
                        self.villian.hp=0
                        self.hp=0
                        print('You run away. Game Over')
                        exit(0)
                else:
                    print('You died. Game Over')
                    exit(0)
                    
            self.wins+=1
            
        print('You Win. Game Over.')
        exit(0)
        

game=Game()

game.start()

    