import requests
import pytesseract as tess
from PIL import Image

def PriceRequest(name, key):
	url = "https://api.tcgplayer.com/catalog/products?categoryId=1&productName=" + name 
	headers = {
				  'Accept': 'text/json',
				  'Authorization': 'bearer ' + key
			  }

	response = requests.request("GET", url, headers=headers)

	## Text processing
	output = (response.text).split(',')
	output = '\n'.join(output)
	output = output.split('{')
	output.pop(1)
	output = ''.join(output)
	output = output.split('\n')


	## Store product ID and set ID

	productIDs = []
	SetID = []


	for word in output:
		if ('productId' in word):
			productIDs.append(word.replace('"productId":',''))
		if ('groupId' in word):
			SetID.append(word.replace('"groupId":',''))

	## Store prices for low, mid, high, market
	## Store set name and printing (foil/non-foil)

	market = []
	low = []
	mid = []
	high = []
	printing = []
	setName = []

	for ID in productIDs:
		prices = requests.request("GET", "https://api.tcgplayer.com/pricing/product/" + ID, headers=headers)
		output = (prices.text).split(',')
		output = '\n'.join(output)
		output = output.split('{')
		output.pop(1)
		output = ''.join(output)
		output = output.split('\n')

		for word in output:
			word = word.replace('}','')
			word = word.replace('[','')
			word = word.replace(']','')
			if ('lowPrice' in word):
				low.append(word.replace('"lowPrice":',''))
			if ('midPrice' in word):
				mid.append(word.replace('"midPrice":',''))
			if ('highPrice' in word):
				high.append(word.replace('"highPrice":',''))
			if ('marketPrice' in word):
				market.append(word.replace('"marketPrice":',''))
			if ('subTypeName' in word):
				foil = word.replace('"subTypeName":','')
				printing.append(foil.replace('"',''))

	for ID in SetID:
		response = requests.request("GET", "https://api.tcgplayer.com/catalog/groups/" + ID, headers=headers)
		output = (response.text).split(',')
		output = '\n'.join(output)
		output = output.split('{')
		output.pop(1)
		output = ''.join(output)
		output = output.split('\n')

		for word in output:
			word = word.replace('}','')
			word = word.replace('[','')
			word = word.replace(']','')
			if('"name":' in word):
				Edition = word.replace('"name":','')
				setName.append(Edition.replace('"',''))
			
	## Output price data
	print('Card: ' + name)
	print('=====================================================================================================')
	print('{: <15}'.format('Low') + '{: <15}'.format('Mid') + '{: <15}'.format('High') + '{: <15}'.format('Market') + '{: <15}'.format('Printing') + '{: <15}'.format('Set'))
	print('=====================================================================================================')

	for x in range(len(low)):
		  data = []
		  data.append(low[x])
		  data.append(mid[x])
		  data.append(high[x])
		  data.append(market[x])
		  data.append(printing[x])
		  data.append(setName[x//2])
		  datastring = []
		  for y in range(len(data)):
			  if (data[y] == 'null'):
				  data[y] = word.replace(word,'N/A')
			  datastring.append('{: <15}'.format(data[y]))
		  print(''.join(datastring))