# Tooling 2

#### Link Collection:

* Using requests + bs4 libraries on python

`response = requests.get('url')`

`soup = BeautifulSoup(response.content, 'html.parser')`

`mainNews = soup.findAll("h2", {"class": "title"})`

`relatedNews = soup.findAll("li", {"class":"related-item"})`

`links = []
for item in news:
    links.append(item.findAll('a', href=True)[0]['href'])`
