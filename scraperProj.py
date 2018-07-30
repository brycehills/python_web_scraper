import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# variable to make url more readbale
my_url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100007709%2050001312%2050001314%2050001315%2050001402%2050001419%2050001471%2050001561%2050001944%2050012150%204814%20601201888%20601204369%20601301599%20601296379%20601296377%2050001669&IsNodeId=1&cm_sp=Cat_video-Cards_1-_-Visnav-_-Gaming-Video-Cards_1'

# vARIABLE = REQUEST FROM URL
uClient = uReq(my_url)

# varibale to store everything pulled from page
page_html = uClient.read()

# close page
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grab header 1
page_soup.h1

#grab body using html
page_soup.body

# grab all items containing specified tag
containers = page_soup.findAll("div", {"class":"item-container"})

for container in containers:
    brand = container.div.div.a.img["title"]
    print(brand)
