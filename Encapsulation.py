class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
# change the price
#c.__maxprice = 1000
c.sell()
print(c.__dict__)
print(c._Computer__maxprice) #this is how to access private method
# using setter function
#c.setMaxPrice(1000)
#c.sell()