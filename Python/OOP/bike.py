import random
class bike(object):
    def __init__(self):
        print 'New Bike!!!'
        self.price = 300
        self.max_speed = 23
        self.miles = 0


    def display_all(self):
        print [self.price, self.max_speed, self.miles]
        return self

    def ride(self):
        print "Riding"
        self.miles +=10
        return self


    def reverse(self):
        if self.miles > 0:
            print "Reversing"
            self.miles -=5
        return self


bike1 = bike()
bike2 = bike()
bike3 = bike()

bike1.ride().ride().ride().reverse().ride().display_all()
