# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 23:33:05 2018

@author: Spikee
"""


from SearchEngine import SearchEngine
from flask import Flask, render_template, request
app = Flask(__name__)



@app.route('/')
def hello():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      query = request.form["query"]
      print(query)
      res=SearchEngine(query)
      
      
      return render_template("result.html",result = res)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='localhost', port=8080)
    
