#To find max number from given two numbers
max = lambda x, y: x if x>y else y
a, b = [int(n) for n in input("enter two numbers").split(' ')]
print("bigger number is {}".format(max(a,b)))

#Lambdas with filter function
x = range(1,100)
lst=list(filter(lambda x: (x%2==0) , x))
print(lst)

#Lambdas with map function
y=range(1,100)
lst1=list(map(lambda x: x**3, y))
print(lst1)

#lambdas with reduce function
from functools import reduce
z = range(500,1000,5)
lst2= reduce(lambda i, j: i*j, z)
print(lst2)