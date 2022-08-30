states = {
      'oregon': 'OR',
      'Florida': 'FL',
      'california': 'CA',
      'New york': 'NY',
      'Michigan': 'MI'
}
cities = {
       'CA': 'San fransico',
       'MI': 'Detroit',
       'FL': 'Jacksonville'
}

cities['NY'] = 'new york'
cities['OR'] = 'Portland'

print('-' * 10)
print("NY state has:", cities['NY'])
print("OR State has: ", cities['OR'])

print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("florida's abbreviation is: ", states['Florida'])

print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

print('-' * 10)
for state, abbrev in list(states.items()):
  print(f"{state} is abbreviated {abbrev}")

print('-' * 10)
for abbrev, city in list(cities.items()):
  print(f"{abbrev} has the city {city}")

print('-' * 10)
for state, abbrev in list(states.items()):
  print(f"{state} state is abbreviated {abbrev}")
  print(f"and has city {cities[abbrev]}")

print('-' * 10)
state = states.get('Texas')
if not state:
     print("sorry no texas.")

city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
