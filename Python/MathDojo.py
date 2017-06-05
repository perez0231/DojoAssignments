class mathdojo(object):
    def __init__(self):
        self.total = 0


    def add(self, num):
        if type(num)== tuple:
            print "touple"
            print num[0]
            print num[1]
            self.total = self.total + (num[0] + num[1])
            return self
            print self.total

        else:
            print "adding.."
            self.total = self.total + num
            return self


    def sub(self, num):
        if type(num)== tuple:
            self.total = self.total - (num[0] + num[1])
            print self.total
            return self
        else:
            self.total = self.total - num
            return self



    def result(self):
        print self.total

math=mathdojo()

math.add(100).sub(2).add((1,2)).sub((1,2))
