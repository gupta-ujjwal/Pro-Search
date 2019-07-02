# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 23:33:05 2018

@author: Spikee
"""
from Results import getResults
from SearchEngine import SearchEngine
from flask import Flask, render_template, request
import time
import csv

app = Flask(__name__)

matrix = []

def readFile():
    global matrix
    with open('StackOverflow.csv', 'r',encoding = "ISO-8859-1") as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            matrix.append(row)
        csvFile.close()

@app.route('/')
def hello():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      s = time.time()
      query = request.form["query"]
      res=SearchEngine(query,matrix)
      res=getResults(res[0:15]) 
      e = time.time()
      print(s-e)
      return render_template("result.html",result = res, query = query)

if __name__ == '__main__':
    readFile()
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='localhost', port=5000)
    