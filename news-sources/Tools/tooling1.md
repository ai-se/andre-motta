# Tooling 1

#### Link Collection:

* Using requests + bs4 libraries on python

`response = requests.get('url')`

`soup = BeautifulSoup(response.content, 'html.parser')`

`news = soup.findAll("h3", {"class": "cd__headline"})`

`links = []
for item in news:
    links.append(item.findAll('a', href=True)[0]['href'])`
    
#### Data Collection:

For each link perform a 

`response = requests.get('url')`

`soup = BeautifulSoup(response.content, 'html.parser')`

collect the Title using the tag: `<h1 class="pg-headline">`

collect the content using the tag `<section class="zn-body-text">`

clean the content by removing the html and absorbing only the text.
