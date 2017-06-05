class car(object):
    def __init__(self, price, speed, fuel, milage):
        print "new Car"
        self.price =  price
        self.speed = speed
        self.fuel = fuel
        self.milage = milage
        if self.price > 10000:
            self.tax= .15
        else:
            self.tax= .12


focus= car(5000, 55, 35, 0)
civic= car(6000, 59, 40, 0)
rougue= car(8000, 50, 30, 0)
explorer= car(10001, 45, 25, 0)
Mustang= car(15000, 75, 20, 0)
Porshue= car(30000, 96, 18, 0)


def display_all(self):
    print [self.price, self.speed, self.fuel, self.milage, self.tax]
    return self
display_all(Porshue)
