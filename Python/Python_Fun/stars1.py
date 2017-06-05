def star(arr):
    for x in arr:
        if type(x) == int:
            star= "*" * x
            print star
        else:
            x= x.lower()
            x = x[0]*len(x)
            print x
star([4, "tom", "Jerry", "Bill", 2, 9, 10])
