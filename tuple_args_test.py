def mypos():
    x=0
    y=0
    return x, y
    
def move(x, y):
    x+=1
    y+=1
    return x,y
    
print("Running test:")
print( mypos() )
print( move( *mypos() ) )