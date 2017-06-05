class product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        print "New Proucts"
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
        self.price = self.price *1.1
        print "taxed"

    def display_all(self):
        print [self.price, self.item_name, self.weight, self.brand, self.cost, self.status]
        return self
    def returnproduct(self, reason):
        if reason == "defective":
            print "defective"
            self.status= "defective"
            self.price = 0
            return self
        if reason == "returned  unopened box":
            print "return to sale"
            self.status= "for Sale"
            return self
        if reason == "returned opened box":
            print "USED"
            self.status= "Used product"
            self.price = self.price * .8 
            return self


soda = product(2, "coke", 1, "Coke", .5)

# soda.sold()
# soda.tax()
# soda.display_all()
# soda.returnproduct(reason = "defective").display_all()
# soda.returnproduct(reason = "returned  unopened box").display_all()
soda.returnproduct(reason = "returned opened box").display_all()
