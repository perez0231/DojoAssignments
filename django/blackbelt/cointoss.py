import random

def flip():
    coin_toss= 5000
    attempt =0
    heads= 0
    tails =0
    count = 1
    print "Initializing program..."
    while in range (0, coin_toss):
        random_num= random.random()
        random_num= random.randint(0,101)

        if (random_num >= 50):
            heads+=1
            print "Attempt #" str(count), "Throwing a coin.. Its a heads! Got" str(heads) "head(s) and" str(tails) "tails thus far"

        else:
            tails += 1
            print "Attempt #" str(count), "Throwing a coin.. Its a heads! Got" str(heads) "head(s) and" str(tails) "tails thus far"

        count 1+=
        print "End of Program"


flip()
