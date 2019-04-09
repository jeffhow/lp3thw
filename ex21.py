def add(a,b):
    print(f"ADDING {a} + {b}")
    return a+b
    
def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a-b
    
def mult(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a*b
    
def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return a/b
    
print("Let's do some math with functions!")

age = add(30,5)
height = subtract(78,4)
weight = mult(90,2)
iq = divide(100,2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzel for extra credit
print("Here is a puzzel.")

what = add(age, subtract(height, mult(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you so it by hand?")