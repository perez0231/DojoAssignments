# def oddeven():
#     for num in range (1,2001):
#         if(num % 2 != 0):
#             print "Number is", + num, ". This is a odd number."
#         if(num % 2 == 0):
#             print "Number is", + num, ". This is a even number."
#



x = [2,4,6,8,10]  #arr values
def multiply(x, y): #function with parameter input and multilier
    arr= []
    for item in x:
        arr.append(item*y)
    print arr

multiply([2,4,6,8,10], 5)
