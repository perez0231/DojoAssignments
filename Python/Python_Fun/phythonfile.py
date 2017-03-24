var =42
var= "new data input"
var2 = var + "1"
print var2

print "My name is var", var


first="Zen"
last= "coder"
print "My name is {}{}". format(first, last)

my_string = 'capitalize this world'
print my_string.capitalize()


my_string2 = 'Lower this world'
print my_string2.lower()

my_string3 = 'Hello WORLD'
print my_string3.swapcase()
# the output would be:
# hELLO world

my_string4 = 'hello world im pissed off'
print my_string4.upper()
# the output would be:
# HELLO WORLD

my_string5 = "by3 hi hi bye bye"
print my_string5.find("hi")
# the output would be:
# 1


my_string6 = "hello world"
print my_string6.replace("world", "mom")
# the output would be:
# hello kitty


my_string7 = "dog, dog, cat, dog, and dog"
print my_string7.replace("dog", "cat", 2)
# the output would be:
# Spam, Spam, Spam, egg and Spam
# notice that only the first 2 "egg" matches were replaced in the string.

ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
newlist= ninjas + my_list
print newlist[4]

newlist=[12,2,4,5,7,83,5,]
newlist.append(69)
print newlist

newlist=[12,2,4,5,7,83,5,]
newlist.insert(1,1000)
print newlist

newlist=[12,2,4,5,7,83,5,]
newlist.remove(2)
print newlist

newlist=[12,2,4,5,7,83,5,]
newlist.pop()
print newlist

newlist=[12,2,4,5,7,83,5,]
newlist.pop(2)
print newlist

newlist=[12,2,4,5,7,83,5,]
newlist.sort()
print newlist

x = [99,4,2,5,-3,12,2,4,5,7,83,5];
print x[1:6]
print x[:6]
print x[3:]


x = [99,4,2,5,-3,12,2,4,5,7,83,5];
print len(x)

x = [99,4,2,5,-3,12,2,4,5,7,83,5];
print max(x)

x = [99,4,2,5,-3,12,2,4,5,7,83,5];
print min(x)

x = [99,4,2,5,-3,12,2,4,5,7,83,5];
print any(x)
