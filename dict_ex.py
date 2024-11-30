states = {
    'Uttar Pradesh': 'UP',
    'Madhya Pradesh': 'MP',
    'Uttrakhand': 'UK',
    'Rajasthan': 'RJ',
    'Gujarat': 'GJ'  
}

cities = {
    'UP': 'Lucknow',
    'MP': 'Bhopal',
    'UK': 'Dehradun',
    'RJ': 'Jaipur'
}

cities['KN'] = 'Kanpur'
cities['DL'] = 'Delhi'
cities['GJ'] = 'Gandhinagar'  

print('-' * 10)
print("UP State has: ", cities['UP'])
print("MP state has: ", cities['MP'])

print('-' * 10)
print("Uttar Pradesh's abbreviation is: ", states['Uttar Pradesh'])
print("Rajasthan's abbreviation is: ", states['Rajasthan'])

print('-' * 10)
print("Uttar Pradesh has: ", cities[states['Uttar Pradesh']])
print("Rajasthan has: ", cities[states['Rajasthan']])

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")
    
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities.get(abbrev, 'No City Found')}")  # Safely access city
    
print('-' * 10)
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")
    
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
