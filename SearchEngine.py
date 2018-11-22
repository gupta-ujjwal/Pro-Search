import csv
matrix = []
doc = []

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

def retrieveDocs():
    global doc,matrix,vis_links,query
    for k in query:
        for i in range(n):
            if(matrix[i][0] == k):
                for j in range(1,m):
                    if (float(matrix[i][j])>0.8) and vis_links[j] not in doc:
                        doc.append(vis_links[j])

readFile()

n = len(matrix)
vis_links = matrix[n-1]
matrix=matrix[0:n-1]
n = n-1
m = len(matrix[0])-1


query = filterToken(input("Enter Query - ").lower().split(' '))

retrieveDocs()

