Takes an image of an MTG card as an input and uses pytesseract to obtain the card name.
Uses this card name to contact the tcgplayer.com API to obtain the metadata about the card.
Prints out the price data for the card in a human readable format.


The input will be selected by the user via file browser
card.jpg shows an example of an input image
Due to the way the ImgToTxt processes the image, the card must take the entirety of the image.
