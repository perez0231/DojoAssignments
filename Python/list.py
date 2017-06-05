str=  "Its thanksgiving day. Its my birthday too!"

print str.find("day")

print str.replace("day", "month")

x= [2, 54,-2, 7, 12, 98]
print max(x)
print min(x)

print x[0], x[len(x)-1]


x = [19,2,54,-2,7,12,98,32,10,-3,6]
newlist=[]

x.sort()
print x

newfirst= x[:5]
print newfirst

newsecond= x[5:]
print newsecond


newsecond.insert(0,newfirst)
print newsecond
