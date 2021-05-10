names = ["mani", "teja", "achari", "19122007", "msc"]
newlist = []

for x in names:
  if "a" in x:
      print(x,end=' ')
      newlist.append(x)

print(newlist)

#List comprehension
newlist = [x for x in names if "a" in x]
print(newlist)

matrix = [[j for j in range(5)] for i in range(5) ]
print(matrix)

planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]
  
# Nested List comprehension with an if condition
flatten_planets = [planet for sublist in planets for planet in sublist if len(planet) < 6]
          
print(flatten_planets)