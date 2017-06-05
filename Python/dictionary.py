me = {"Name": "Daniel", "Age": "29", "POB":"The US", "FavLang": "Python"}

shadow = {"Name": "Shadow", "Age": "89", "POB":"The US", "FavLang": "puppy"}

Peter = {"Name": "Pete", "Age": "21", "POB":"The Neatherlands", "FavLang": "C+"}


def printing(arg):
    print "My name is", arg["Name"]
    print "My age is", arg["Age"]
    print "I was born in", arg["POB"]
    print "My fav lang is", arg["FavLang"]




printing(shadow)
