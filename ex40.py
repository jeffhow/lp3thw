# Standard Dictionary
mystuff = {'apple':'I AM APPLES!'}
print(mystuff['apple'])

# Module way
import mystuffmodule
mystuffmodule.apple()
print(mystuffmodule.tangerine)

# Class way
from mystuffclass import MyStuff

thing = MyStuff()
thing.apple()
print(thing.tangerine)

print('-'*10)
### Official ex40 Code
class Song: # in Python3, object inheritance is implicit in classes. eg.: class Song(object): is an obsolete syntax.
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

s1 = Song(['line 1', 
            'line 2', 
            'line 3'])
            
s2 = Song(['line 1', 
            'line 2'])

s1.sing_me_a_song()

s2.sing_me_a_song()