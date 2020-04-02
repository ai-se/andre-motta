# Tooling 3

#### Link Collection:

* Using requests + bs4 libraries on python

`response = requests.get('url')`

`soup = BeautifulSoup(response.content, 'html.parser')`

`mainNews = soup.findAll("a", {"class": "gs-c-promo-heading"})`


`links = []
for item in news:
    links.append(item['href'])`
    


