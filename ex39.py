# Create a mapping of state to abbreviation
states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI',
}

# Create a basic set of states and some cities in them
cities = {
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville',
}

# Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portaland'

# Print out some cities
print('-'*10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

# Print some states
print('-'*10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# Use the dictionaries for cities
print('-'*10)
print("Michigan's has: ", cities[states['Michigan']])
print("Florida's has: ", cities[states['Florida']])

# Print Every state abbrev
print('-'*10)
for state, abbrev in list( states.items() ):
    print(f"{state} is abbreviated {abbrev}")

# Print every city in state
print('-'*10)
for city, abbrev in list( cities.items() ):
    print(f"{abbrev} has the city {city}")

# now do both at same time
print('-'*10)
for state, abbrev in list( states.items() ):
    print(f"{state} has the abbreviation: {abbrev}")
    print(f"{abbrev} has the city: { cities[abbrev] }")

print('-'*10)
#Safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")
    
# Get City safely another way by providing a default value
city = cities.get('TX', "Does not exists, my dude.")
print(f"The City for the state 'TX' is: {city}")