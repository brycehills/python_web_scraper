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

#grab body
page_soup.body

# grab all items containing specified tag
containers = page_soup.findAll("div", {"class":"item-container"})

num_products = len(containers)

info = page_soup.findAll("div", {"class":"item-info"})

# ******************* begin for loop *************************************
for i in info:
    # grabs title of item
    brand = i.div.a.img["title"]

    # grab name block
    nameContainer = i.findAll("a",{"class","item-title"})
    name = nameContainer[0].text.strip("Video Card")

    # grabs price area within item container block
    priceContainer = i.findAll("li" , {"class":"price-current"})
    # grabs actual price of item
    price = priceContainer[0].strong.text

    # grabs ratin block
    ratingContainer = i.findAll("a", {"class","item-rating"})

    # check if the container exists
    if ratingContainer:
        # if exists give it its proper string value
        rating = ratingContainer[0]["title"].strip("Rating + ")
        # append stars for readability
        rating += " stars"
    else:
        # if does not exist display not found
        rating = "No rating found"


    shippingContainer = i.findAll("li",{"class","price-ship"})
    shipping = shippingContainer[0].text.strip()

    # iterate and print info - can only concat(+) with str
    print("BRAND:    " + brand)
    # print(nameContainer)
    print("NAME:     " + name)
    print("PRICE:    $" + price + ".00 USD")
    print("SHIPPING: " + shipping)
    print("RATING:   " + rating)
    print("") # newline for readability in output

    # next scrape to output file

# *********************** end for loop ***********************************



# syntax for findall:
# beginning tag , following tag = label
