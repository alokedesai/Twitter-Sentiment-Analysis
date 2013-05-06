import sys
import json


def test (sf, tf):
    uncoded = []
    decodedText=[]
    for x in tf.readlines():
        y= json.loads(x)
        if y.has_key("place"):
            #uncoded.append(y["text
            if y["place"] != None and y["place"]["country"] == "United States" and y["place"]["country_code"] == "US":
                #decodedText.append((y["text"].encode("utf-8")), ((y["place"]["full_name"]).split(",")[1]))
               state= (y["place"]["full_name"]).split(",")[1]
               text = y["text"].encode("utf-8")
               decodedText.append((text,state))

    return decodedText
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
def check(decodedText, op):
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
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    x =test(sent_file, tweet_file)
    y= sfDict(sent_file)
    check (x,y)

if __name__ == '__main__':
    main()
