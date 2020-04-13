from flask import Flask, render_template,request, jsonify,send_from_directory
import json as simplejson
import json
from pymongo import MongoClient
from bson.json_util import dumps
import random
import os
from math import radians, cos, sin, asin, sqrt 
import math

app = Flask(__name__)

client = MongoClient('mongodb://Harilee:harilee1329@haridatabase-shard-00-00-egsq3.mongodb.net:27017,haridatabase-shard-00-01-egsq3.mongodb.net:27017,haridatabase-shard-00-02-egsq3.mongodb.net:27017/test?ssl=true&replicaSet=hariDatabase-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client.MyBlog


@app.route("/")
def parent():
  return render_template("home.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/home")
def home():
  return render_template("home.html")

@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.route("/contact", methods=['POST'])
def contact_post():
  return render_template("contact.html")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/get-articles", methods=['GET'])
def get_article():
  try:

    articleObj = db.article.find()
    if articleObj == None:
      return dumps({
        'result': 'no',
        'data': []
      })
    else:  
      return dumps({
          'result':'yes',
          'data' : articleObj
        })
      
  except Exception as e:
      return dumps({'error' : str(e)})

 
@app.route("/read_article")
def read_article():
  
  return render_template("read_article.html")


@app.route("/get-article-specific/<string:article_id>", methods=['GET'])
def get_article_specific(article_id):
  try:

      article = db.article.find_one({
        'id':article_id
      })
      if article == None:
        return dumps({
          'result':'no',
          'data' : ''
        })
      else:
          return dumps({
          'result':'yes',
          'data' : article
        })
   

  except Exception as e:
      return dumps({'error' : str(e)})

     
@app.route("/see_all")     
def see_all():
  return render_template("see_all.html")


@app.route("/upload_article")
def upload_article():
  return render_template("upload_article.html")


@app.route("/upload_article", methods=['POST'])
def upload_article_post():
  try:
    title = request.form['title']
    body = request.form['article_body']
    desc = request.form['desc']
    author = request.form['name']
    
    count = db.article.count()+1
    articleId ='article00'+str(count)

    upload_status = db.article.insert({
      "title" : title,
      "body" : body,
      "image" : "asas",
      "id" : articleId,
      "author" : author,
      "description" : desc,
      "upvote" : "0",
      "downvote" : "0"

    })
    status = db.article.find_one({"_id": upload_status})
    print (title)
    return render_template('upload_article.html', value="yes")
  except Exception as e:
      return dumps({'error' : str(e)})

if __name__=='__main__':
  app.run(debug=True)  