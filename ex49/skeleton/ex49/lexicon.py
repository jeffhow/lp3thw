import re
def scan(s):
    words = s.split()
    
    lexi = {
        'direction': "north south east west".split(),
        'verb' : "go kill eat".split(),
        'stop' : "the in of".split(),
        'noun' : "bear princess".split(),
    }
    
    phrases=[]
    
    # numbers = re.findall('\d+',s)
    # map() converts this list of str to int (e.g '4' => 4)
    # print(list(map(int,numbers))) 
    # for n in numbers:
    #     phrases.append(('number',int(n)))
    
    for word in words:
        try:
            phrases.append(('number',int(word)))
        except ValueError:
            
            for key in lexi:
                if word in lexi[key]:
                    phrases.append((key, word))
                    break # if found, break the loop
                
            else: # run if the loop wasn't broken
                phrases.append(('error', word))
    
    
    return phrases
