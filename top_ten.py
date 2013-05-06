import sys
import json


def test (tf):
    tweets = []
    decodedText=[]
    for x in tf.readlines():
        y= json.loads(x)
            #uncoded.append(y["text
        if y.has_key("entities") and y["entities"]["hashtags"] != []:
            for x in  y["entities"]["hashtags"]:
                if x["text"].isalnum():
                    tweets.append((x["text"]))
    newTweets ={}
    for i in tweets:
        if i in newTweets:
            newTweets[i] += 1
        else:
            newTweets[i] = 1
    topTen = []
    for w in sorted(newTweets, key=newTweets.get, reverse=True):
        topTen.append((w, newTweets[w]))
    topTen = topTen[0:10]
    for (x,y) in topTen:
        print x + " " + str(y)
    #for x in uncoded:
    #
    #    decodedText.append((x.encode("utf-8")))
    #    
    #return decodedText
def sfDict(sf):
    #x = {}
    #for s in sf.readlines():
    #    y= s.split()
    #    x["pair"] = {
    #        "word" : y[0],
    #        "val" : y[1]
    #    }
    x = []
    for s in sf.readlines():
            y = s .split("\t")
            x.append((y[0], y[1]))
    return x
def check(decodedText):
    states={}
    for (tweet, st) in decodedText:
        val= 0.0
        for (x,y) in op:
            if ((x + " " )  or (" " + x)) in tweet:
                val= val + float(y)
                if st in states:
                    states[st] += val
                else:
                    states[st] = val
    x= 0.0
    finalState = ""
    for key, value in states.iteritems():
        if value > x:
            finalState = key
            x= value
    print finalState
    
def main():
   
    tweet_file = open(sys.argv[1])
    test(tweet_file)

if __name__ == '__main__':
    main()
