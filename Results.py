import urllib.request
from bs4 import BeautifulSoup

result = []

def getResults(links):
    global result
    links = links[::-1]
    while(len(links)>0) :
        link = links.pop()[0]
        temp = []
        temp.append(link)
        try :
            response = urllib.request.urlopen(link)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            mydivs = soup.find("h1", {"class": "fs-headline1"})
            WebText=mydivs.get_text()
            temp.append(WebText)
            result.append(temp)
        except :
            print("Unable to fetch data from link")
            continue
    return result


#how-can-i-get-the-id-of-an-element-using-jquery