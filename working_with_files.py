vi = open("test.txt", 'w')
vi.write("Hello World, This is Mani")
vi.close()
zi = open("test.txt", "r")
print(zi.readlines())

with open("test.txt",'a+',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
   print(f.readlines())