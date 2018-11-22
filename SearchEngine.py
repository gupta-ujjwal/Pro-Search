import csv
import math

matrix = []
doc = []
ranking = []
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
            matrix.append(row)
    csvFile.close()

def column(mat, i):
    return [row[i] for row in mat]

def retrieveDocs():
    global doc,matrix,vis_links,query
    doc.append(column(matrix, 0))
    for k in query:
        for i in range(n):
            if(matrix[i][0] == k):
                for j in range(1,m):
                    if (float(matrix[i][j])>0.8) and vis_links[j] not in links:
                        doc.append(column(matrix, j))
                        links.append(vis_links[j])

readFile()

n = len(matrix)
vis_links = matrix[n-1]
matrix=matrix[0:n-1]
n = n-1
m = len(matrix[0])-1


query = filterToken(input("Enter Query - ").lower().split(' '))

retrieveDocs()

for i in range(len(links)):
    ranking.append(0)
   
queryArray = []
queryAmp = 0
for i in doc[0]:
    if i in query:
        queryArray.append(1)
        queryAmp = queryAmp + 1
    else:
        queryArray.append(0)

queryAmp = math.sqrt(queryAmp)

for i in range(1,len(doc)):
    sum = 0
    amp = 0
    for j in range(len(doc[i])):
        amp = amp + float(doc[i][j])
        if doc[0][j] in query:
            sum = sum + float(doc[i][j])
    amp = math.sqrt(amp)
    ranking[i-1] = sum/(amp*queryAmp)

print(max(ranking))
            



