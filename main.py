from ImgToTxt import ImgToTxt
from PriceRequest import PriceRequest


def main():
	file = open('bearer.json').readlines()
	token = file[0].replace('"','')
	cardname = ImgToTxt()
	PriceRequest(cardname, token)
	
	
	
	
if __name__ == "__main__":
	main()