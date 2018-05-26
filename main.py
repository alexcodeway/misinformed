import requests
from bs4 import BeautifulSoup
from misinformed import subjectiveCount

# the url to a new article
url = "http://www.bbc.com/news/world-us-canada-44243644"

html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
[x.extract() for x in soup.findAll('script')] # strip out scripts

tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'article', 'summary'] # candidates for content
full_text = ''

for tag in tags:
    for x in soup.findAll(tag):
        full_text += (str(x.getText()) + ' ')

count = subjectiveCount(full_text)

print("Total opinionated sentences: " + str(count))
    