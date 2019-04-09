formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one", "Two", "Three", "Four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "My balogna has a first name", 
    "It's OSCAR", 
    "My Balogna has a second name", 
    "It's MEYER"
    ))