myarr= ['magical unicorns',19,'hello',98.98,'world']
sum=0
intcount=0
strcount=0
newstr= "String:"
for i in range(0, len(myarr)):
    if isinstance(myarr[i], (int, float)):
        sum = sum + myarr[i]
        intcount= intcount + 1




    elif isinstance(myarr[i], str):
        newstr= newstr + " " + myarr[i]
        strcount= strcount + 1


if intcount & strcount > 0:
    print "This is a mixed type"
elif strcount > 0:
    print "This array is integer based"
else:
    print "this is string based "


print "Sum: {}".format(sum)
print newstr





# for x in l:
#     if isinstance(x, int):
#         print "this "
