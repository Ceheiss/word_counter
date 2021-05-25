import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Get page to crawl
website_url = input("Enter url of the page you want to crawl:")
html = urllib.request.urlopen(website_url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Words to ignore
prepositions = ['a', 'ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde', 'durante', 'en', 'entre', 'hacia', 'hasta', 'mediante', 'para', 'por', 'según', 'sin', 'so', 'sobre', 'tras', 'versus']
articles_and_pronouns = ['el', 'la', 'los', 'las', 'ella', 'ellos', 'ellas', 'un', 'una', 'nosotros', 'vosotros', 'tú', 'ustedes', 'te', 'mí', 'ti', 'del', 'al', 'su', '|']
conectors = ['y', 'que', 'porque', 'por', 'se', 'no', 'si', 'también']
forbidden_words = prepositions + articles_and_pronouns + conectors

words = []

p_tags = soup.find_all('p')
h1_tags = soup.find_all('h1')
p_tags = soup.find_all('p')
h3_tags = soup.find_all('h3')

def get_words_by_tag(tag, word_list):
  for tag in p_tags:
    # get a list of all words with the tag
    raw_word_list = str(tag.get_text()).lower().split()
    parsed_word_list = []
    # create a list with the parsed words
    for word in raw_word_list:
      if word not in forbidden_words:
        parsed_word_list.append(word)
    # add to main list
    word_list += parsed_word_list

get_words_by_tag('p', words)
get_words_by_tag('h1', words)
get_words_by_tag('h2', words)
get_words_by_tag('h3', words)

print("Current words length:", len(words))

word_counter = {}

for word in words:
    word_counter[word] = word_counter.get(word, 0) + 1

biggestNumber = None
biggestWord = None

for word,times in word_counter.items():
    if biggestNumber == None or times > biggestNumber:
        biggestNumber = times
        biggestWord = word

print(word_counter, biggestWord, biggestNumber)
