# User Story:
# User can search two species and see how closely they are related
# User will see a tree depicting where in the tree of life the species are located with respect to each other
# i.e Pan Troglodyte and Pan Paniscus are one species apart, Pan Troglodyte and Homo Sapiens are one genus apart, etc
# In the case of colloquial name input, if only one species (i.e killer whale): simply find species, else: suggest a list of binomial names
# Show wikipedia.summary of the page to the user

from bs4 import BeautifulSoup
import requests
from html.parser import HTMLParser
import re

page = "https://animaldiversity.org/accounts/orca/"
r = requests.get(page)
soup = str(BeautifulSoup(r.text, "html.parser").find(class_="classification well"))
html_words = []

class MyParser(HTMLParser):
    def handle_data(self, data):
        trying = re.sub(r'\W+', "", data)
        
        if trying != "":
            html_words.append(trying)


def list_to_dick():
    bio = ["Kingdom", "Phylum", "Class", "Order", "Family", "Genus", "Species"]
    nomenclature = {}

    for name in bio:
        if name in html_words:
            nomenclature[name] = html_words[html_words.index(name) + 1]

    # Changes species from binomial name to just species, capitalized
    if "Species" in nomenclature:
        nomenclature["Species"] = nomenclature["Species"].replace(nomenclature["Genus"], "").capitalize()

    return nomenclature


word_parser = MyParser()
word_parser.feed(soup)
dick = list_to_dick()
print(dick)

# Build search feature from taxa.txt and vernacular.txt
# Make a class where you initialize with an animal's name, and the class has a method that creates a dictionary of the animal's full nomenclature

