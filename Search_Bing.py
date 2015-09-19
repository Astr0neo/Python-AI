import bingsearch
bingsearch.API_Key='jD3Z74oQ/rXGkR51VtMZ5HJa7iCyTPMQPrVtKaTALI8'

request = None

def searchbing(criteria):
	request = bingsearch.request(criteria)
	return request[0]['Description']