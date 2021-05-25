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

# Retrieve all a tags
paragraphs = soup('span')
for paragraph in paragraphs:
    print("p:", paragraph)

titles = soup('h1')
for title in titles:
    print("h1:", title)

subtitles = soup('h3')
for subtitle in subtitles:
    print("p:", subtitles)