x = "spaceoisdjf"

if type(x) == int:
    if x >= 100:
        print "That's a big number!"

    else:
        print "small num"
elif type(x) == str:
    if len(x) < 50:
        print "short sentance"
    else:
        print "Long sentance"

else:
    if len(x) >= 10:
        print "big list"
    else:
        print "short list"




#
#
#
# for x in my_str:
#     if isinstance(x, int):
#         print "this is an int type"
#         sum = sum + x
#         print "Sum: {}".format(sum)
#
#         if x >= 100:
#             print "That's a big number!"
#
#         else:
#     print "small num"
#
#
# sS = "Rubber baby buggy bumpers"
# mS = "Experience is simply the name we give our mistakes"
# bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
#
#
# if len(bS) < 50:
#     print "short sentance"
# else:
#     print "Long sentance"
#
#
# aL = [1,7,4,21]
# mL = [3,5,7,34,3,2,113,65,8,89]
# lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
# eL= [],
# spL = ['name','address','phone number','social security number']
#
# if len(spL) >= 10:
#     print "big list"
# else:
#     print "short list"
