# -*- coding: utf-8 -*-

while(len(vis_links)<7000) :
    if (links.empty()!=True) :
        link = links.get()
        print(len(vis_links))
        vis_links.append(link)
        try :
            response = urllib.request.urlopen(link)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            mydivs = soup.findAll("div", {"class": "question"})
            WebText=''
            tdTags=[]
            for tag in mydivs:
                tdTags = tag.find_all("p")
            for elem in tdTags:
                WebText = WebText+' '+elem.get_text()
            WebText=WebText.lower() 
            tokens = filterToken(WebText.split(' '))
            addToDict(tokens,link,WebText)
            
          #tokens = 
            for element in soup.find_all('a'):
                if element.get('href') and '/questions/' in element.get('href') and element.get('href') not in vis_links and 'tagged' not in element.get('href'):
                    temp = element.get('href')
                    if 'http' in temp:
                        if 'stackoverflow.com' in temp:
                            links.put(temp)
                    else:
                        temp = 'https://stackoverflow.com'+temp
                        if temp not in vis_links:
                            links.put(temp)
        except :
            print("Unable to fetch data from link")
            continue
        
    else :
        print("No Further Links")
        break

