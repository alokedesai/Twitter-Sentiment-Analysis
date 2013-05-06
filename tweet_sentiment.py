import sys
import json
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def test (sf, tf):
    uncoded = []
    decodedText=[]
    for x in tf.readlines():
        y= json.loads(x)
        if y.has_key("text"):
            uncoded.append(y["text"])
    
    for x in uncoded:
    
        decodedText.append((x.encode("utf-8")))
        
    return decodedText
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
    for z in decodedText:
        val= 0.0
        for (x,y) in op:
            if ((x + " " )  or (" " + x)) in z:
                val= val + float(y)
        print z + "  : " + str(val)
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    x =test(sent_file, tweet_file)
    y= sfDict(sent_file)
    check (x,y)

if __name__ == '__main__':
    main()
