from sys import argv

script, arg = argv
n = int(arg)

for i in range( 1, n ):
    if n//i == i and n%i == 0:
        print(n//i)
        exit(0)
        
print(False)