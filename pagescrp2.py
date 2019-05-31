'''
INPUT: Alter title to grab.

OUTPUT: Grabs title of website.

'''
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def get_title(url):
    try:
        html_ = urlopen(url)
    except HTTPError as err:
        return None
    try:
        bs_obj = BeautifulSoup(html_.read(), "lxml")
        title = bs_obj.body.h1
    except AttributeError as err:
        return None
    return title

title_ = get_title("http://www.pythonscraping.com/pages/page1.html")
if title_ == None:
    print("Title could not be found")
else:
    print(title_)
