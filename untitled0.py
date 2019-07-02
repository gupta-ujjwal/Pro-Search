# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 14:58:53 2018

@author: asus
"""

import csv
import math

#packet class
class packet(object):
    url = ""
    val = 0
    score = 0
   
    # The class "constructor" - It's actually an initializer 
    def __init__(self):
        self.rep = ""
        self.url = 0
        self.score = 0
    
matrix = []
doc = []
links = []

def filterToken(tokens):
    for a in tokens:
        if len(a)>0 and (a[len(a)-1] == '.' or a[len(a)-1] == ',' or a[len(a)-1] == '!' or a[len(a)-1] == '?') :
            tokens[tokens.index(a)]=a[0:len(a)-1]
                
    tokens = [''.join([a for a in str if a.isalpha() or a.isdigit()]) for str in tokens if len(str)>0]          
    return tokens
    
def readFile():
    global matrix
    with open('StackOverflow.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            print(row)
            matrix.append(row)
        csvFile.close()
    
def column(i):
    global matrix
    return [row[i] for row in matrix]

def retrieveDocs(query,m,vis_links,n):
    global doc,matrix
    doc.append(column(0))
    for k in query:
        for i in range(n):
            if(matrix[i][0] == k):
                for j in range(1,m):
                    if (float(matrix[i][j])>0) and [vis_links[j-1],0] not in links:
                        doc.append(column(j))
                        links.append([vis_links[j-1],0])

                        
def SearchEngine(query):
    global matrix
    global doc,ranking,links
    readFile()
    n = len(matrix)
    vis_links = matrix[n-1]
    matrix=matrix[0:n-2]
    n = n-2
    m = len(matrix[0])-1
    query = filterToken(query.lower().split(' '))
    doc=[]
    retrieveDocs(query,m,vis_links,n)
       
    queryArray = []
    queryAmp = 0
    for i in doc[0]:
        if i in query:
            queryArray.append(1)
            queryAmp = queryAmp + 1
        else:
            queryArray.append(0)
    
    queryAmp = math.sqrt(queryAmp)
    
    #cosine similarity
    for i in range(1,len(doc)):
        sum = 0
        amp = 0
        for j in range(len(doc[i])):
            amp = amp + float(doc[i][j])**2
            if doc[0][j] in query:
                sum = sum + float(doc[i][j])
        amp = math.sqrt(amp)
        links[i-1][1] = sum/(amp*queryAmp)
    
    #Sorting and filtering based on cosine score
    n = len(links) 
    for i in range(n):
        for j in range(0, n-i-1):
            if links[j][1] < links[j+1][1] :
                links[j], links[j+1] = links[j+1], links[j]
                
    links = [a for a in links if a[1]>0.08 and (not links[links.index(a)+1][1] == a[1] or links.index(a) == n-1 )]          
    
    return links
        
    