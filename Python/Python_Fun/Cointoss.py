import random

def scores():
    num_scores= 5000
    heads=0
    tails=0
    count=1
    print "Starting the Program..."
    for scores in range (0,num_scores):
        random_num = random.random()
        random_num =random.randint(1,101)
        if(random_num >= 50):
            heads+=1
            print "Attempt #", str(count), "Throwing a coin.. Its a heads! Got", str(heads), "head(s) and", str(tails), "tail(s) so far"
        else:
            tails+=1
            print "Attempt #", str(count), "Throwing a coin.. Its a tails! Got", str(heads), "head(s) and", str(tails), "tail(s) so far"
        count+=1
        print "Ending the Program, thank you!"



scores()
