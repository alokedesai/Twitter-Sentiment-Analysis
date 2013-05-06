import sys
import json

    
def test (tf):
    uncoded = []
    decodedText=[]
    for x in tf.readlines():
        y= json.loads(x)
        if y.has_key("text"):
            uncoded.append(y["text"])
    
    for x in uncoded:
    
        decodedText.append((x.encode("utf-8")))
        
    return decodedText

def calc (decodedText):
    totalWords = 0.0
    words = {}
    for x in decodedText:
        
        for word in x.split():
            totalWords += 1
            if word in words:
                x = (words)[word] + 1.0
                words[word] = x
            elif word.isalnum() or "," in word:
                words[word] = 1.0

    for x in range(len(words)):
        print words.keys()[x] + " " + str(words.values()[x] / totalWords)
def main():
    sent_file = open(sys.argv[1])
    x= test(sent_file)
    calc(x)
if __name__ == '__main__':
    main()
