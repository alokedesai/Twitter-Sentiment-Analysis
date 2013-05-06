import urllib
import json
for x in range(1,10):
          
          response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft&page=" + str(x) )
          for x in json.load(response)[u'results']:
                    print x[u'text']