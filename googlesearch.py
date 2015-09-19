#!/usr/bin/python3
import json
import urllib.request, urllib.parse
import re


#def showsome(searchfor):
  #query = urllib.parse.urlencode({'q': searchfor})
  #url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
  #search_response = urllib.request.urlopen(url)
  #search_results = search_response.read().decode("utf8")
  #results = json.loads(search_results)
  #data = results['responseData']
  #print('Total results: %s' % data['cursor']['estimatedResultCount'])
  #hits = data['results']
  #print('Top %d hits:' % len(hits))
  #for h in hits: 
    #print(' ', h['url'])
    #print('For more results, see %s' % data['cursor']['moreResultsUrl'])
    #print(h['content'])

#showsome('transvision vamp')

def geturl(id, criteria):
  query = urllib.parse.urlencode({'q': criteria})
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
  search_response = urllib.request.urlopen(url)
  search_results = search_response.read().decode("utf8")
  results = json.loads(search_results)
  data = results['responseData']
  hits = data['results']
  return hits[id]['url']

def getcontent(id,criteria):
  query = urllib.parse.urlencode({'q': criteria})
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
  search_response = urllib.request.urlopen(url)
  search_results = search_response.read().decode("utf8")
  results = json.loads(search_results)
  data = results['responseData']
  hits = data['results']
  response = hits[id]['content']
  return response

print(geturl(0,'transvision vamp'))

r = getcontent(0,'transvision vamp')
r_list = list(r)
print(r_list)