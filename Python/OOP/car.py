import random
class car(object):
  def __init__(self, price, speed, fuel, milage):
    print 'New car!!!'
    self.price = price
    self.speed = speed
    self.fuel = fuel
    self.milage = milage

    if price > 1000:
        self.tax = .15
    else:
        self.tax= .12


print dir(car)

focus= car(1000, 45, 35, 30)
bronco= car(3000, 50, 10, 50)
mustang= car(5000, 70, 29, 80)
rogue= car(3000, 60, 25, 80)
escape= car(1000, 45, 29, 70)
porshe= car(10000, 120, 20, 20)



def display_all(self):
    print [self.price, self.speed, self.fuel, self.milage, self.tax]
    return self
display_all(rogue)

# n the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage.

# If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%.
