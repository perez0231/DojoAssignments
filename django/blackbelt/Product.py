class product(object):
    def __init__(self, price, item_name, weight, brand, cost, status):
        print "new Car"
        self.price =  price
        self.item_name= item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for Sale"


    def sold(self):
        self.status = "sold"
        print "SOLD!"
        return self

    def tax(self):
        self.status = cost *1.1


soda = product(2, coke, 1, Coke, .5)
