import urllib.request
from bs4 import BeautifulSoup
import queue
import math
import string
from collections import defaultdict
from array import *
import csv

links = queue.Queue(maxsize=0)
preLinks = ['https://stackoverflow.com/questions','https://stackoverflow.com/questions/tagged/php','https://stackoverflow.com/questions/tagged/xml','https://stackoverflow.com/questions/tagged/c%23','https://stackoverflow.com/questions/tagged/react-native','https://stackoverflow.com/questions/tagged/sql','https://stackoverflow.com/questions/tagged/jquery','https://stackoverflow.com/questions/tagged/ios','https://stackoverflow.com/questions/tagged/javascript','https://stackoverflow.com/questions/tagged/node.js','https://stackoverflow.com/questions/tagged/python','https://stackoverflow.com/questions/tagged/algorithm','https://stackoverflow.com/questions/tagged/java','https://stackoverflow.com/questions/tagged/android']
for i in preLinks:
    links.put(i)
vis_links = []
tokens = []
dictonary = defaultdict(list)
WebText = ''
matrix = [[]]

class packet(object):
    url = ""
    rep = 0
   
    # The class "constructor" - It's actually an initializer 
    def __init__(self):
        self.rep = ""
        self.url = 0
    
def filterToken(tokens):
    for a in tokens:
        if len(a)>0 and (a[len(a)-1] == '.' or a[len(a)-1] == ',' or a[len(a)-1] == '!' or a[len(a)-1] == '?') :
            tokens[tokens.index(a)]=a[0:len(a)-1]        
    tokens = [''.join([a for a in str if a.isalpha() or a.isdigit()]) for str in tokens if len(str)>0]          
    return tokens
    
def addToDict(tokens,url,text):
    global dictonary
    tokens = set(tokens)
    for i in tokens:
        obj = packet()
        rep = text.count(i)
        obj.url = url
        obj.rep = rep/len(text.split(' '))
        dictonary[i].append(obj)
 
def generateMatrix():
    global dictonary,vis_links,matrix
    n = len(dictonary)
    m = len(vis_links)
    matrix = [[0]*(m+1) for i in range(n)]
    c = -1
    for i in dictonary:
        c = c+1
        tf = 0
        idf = 0
        matrix[c][0] = i
        for j in range(1,m+1):
            for k in dictonary[i]:
                if(k.url == vis_links[j-1]):
                    tf = k.rep
                    idf = math.log(m/len(dictonary[i]))
                    matrix[c][j]=round(tf*idf, 2)
                    break
            else:
                matrix[c][j]=0
                
def storeMatrix(matrix):
    csvfile = "StackOverflow.csv"
    global vis_links
    matrix.append(vis_links)
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for val in matrix:
            try:
                writer.writerow(val)  
            except:
                print(val[0])
                continue
    
#Crawler       
while(len(vis_links)<10000) :
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


generateMatrix()
storeMatrix(matrix)