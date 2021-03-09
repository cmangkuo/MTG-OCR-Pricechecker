import pytesseract as tess
from PIL import Image
import os
import easygui




def ImgToTxt():
	## Load card image
	filepath = easygui.fileopenbox()
	card = (Image.open(filepath)).convert('L')
	
	## Process card image
	card = card.resize((488,680))		## Resize card image
	crop = card.crop((40,30,350,75))	## Crop image to area of relevant text
	
	## Save cropped card image
	crop.save('crop.jpg')
	
	## Extract text from cropped card image
	cardname = tess.image_to_string('crop.jpg')
	
	## Process text
	cardname.replace('\x0c','')		## Remove unknown characters
	cardname.replace('\n','')		## Remove newline characters  
	cardname = cardname.strip()		## Strip leading and trailing spaces
	

	os.remove('crop.jpg')		## Delete the cropped card image
	return cardname				## Return the name of the card
	
	
if __name__ == "__main__":
	print(ImgToTxt())