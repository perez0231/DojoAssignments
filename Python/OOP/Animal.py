class animal(object):
    def __init__(self, name):
        print "new Animal"
        self.name = name
        self.health =100

    def walk(self):
        self.health -=1
        return self

    def run(self):
        self.health -=5
        return self

    def displayHealth(self):
        print[self.name, self.health]
        return self


animal1= animal("Peter")
animal1.displayHealth()
# animal1.pet()
# class animal(animal):
#     def __init__(self, name, health):
class dog(animal):
    def __init__(self, name):
        super(dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health +=5
        return self

animal2 = dog("charles")

animal2.walk().walk().walk().run().run().pet().displayHealth()
# animal2.fly()
class dragon(animal):
    def __init__(self, name):
        super(dragon, self).__init__(name)
        self.health = 170
        print "Dragon Made"

    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        print "I am dragon"
        print[self.name, self.health]
        return self

animal3 = dragon("Dragoon")

animal3.walk().walk().walk().run().run().fly().fly().displayHealth()
