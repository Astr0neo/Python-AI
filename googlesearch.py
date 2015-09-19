#!/usr/bin/python3
import json
import urllib.request, urllib.parse

temp_value = None
temp_index1 = None
temp_index2 = None

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
  answer = splitup(response)
  return answer

def splitup(data):
  answer = ""
  r_list = list(data)

  while '<' in r_list:
    temp_index1 = r_list.index('<')
    temp_index2 = r_list.index('>')

    if '/' in r_list:
      if r_list.index('/') >= temp_index1 and r_list.index('/') <= temp_index2:
        r_list[(r_list.index('/'))] = ''

    if 'b' in r_list:
      if r_list.index('b') >= temp_index1 and r_list.index('b') <= temp_index2:
        r_list[(r_list.index('b'))] = ''

    if '>' in r_list:
      if r_list.index('>') >= temp_index1 and r_list.index('>') <= temp_index2:
        r_list[(r_list.index('>'))] = ''

    if '<' in r_list:
      if r_list.index('<') >= temp_index1 and r_list.index('<') <= temp_index2:
        r_list[(r_list.index('<'))] = ''

  r_list[(r_list.index('\xa0'))] = ''
  r_list[(r_list.index('\n'))] = ''

  for item in r_list:
    answer += item

  answer = answer.split('.')
  return(answer[0])    

print(geturl(0,'transvision vamp'))
print(getcontent(0, 'transvision vamp'))