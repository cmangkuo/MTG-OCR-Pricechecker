from image_to_text import image_to_text
from price_request import price_request


def main():
    file = open("bearer.json").readlines()
    token = file[0].replace('"', "")
    card_name = image_to_text()
    price_request(card_name, token)


if __name__ == "__main__":
    main()
