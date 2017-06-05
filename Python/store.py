class store(object):
    def __init__(self,location, owner):
        print "New store"
        self.products = []
        self.location= location
        self.owners = owner

    def addproduct(self, product):
        print "here"
        self.products.append(product)
        return self
    def remove(self, product):
        print
    def display_all(self):
        print(self.products, self.location, self.owners)

ralphs = store("oxnard", "tim")
ralphs.addproduct("chips").addproduct("lemons")
ralphs.addproduct("soda")
ralphs.display_all()
