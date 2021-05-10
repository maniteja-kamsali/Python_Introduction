#To find max number from given two numbers
max = lambda x, y: x if x>y else y
a, b = [int(n) for n in input("enter two numbers").split(' ')]
print("bigger number is {}".format(max(a,b)))