def sortDictByKey( d ):
    keys=[]
    
    for key, value in list(d.items()):
        keys.append(key)
        
    keys.sort()
    
    temp={}
    
    for key in keys:
        temp[key] = d[key]
        
    return temp
    
test = {'a':'foo', 'z':'bar', 'f':'fizbar'}

print( sortDictByKey( test ) )