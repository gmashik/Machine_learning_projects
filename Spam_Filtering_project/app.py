import flask
from flask import Flask, request, render_template
import json
import joblib
import random
import string
import sklearn

def text_processing(instr): #tokenizing 
  """
  1. Remove punctuation form each message 
  2. Remove Stop words
  3. Return processed words
  """
  puncremove=[word for word in instr if word not in string.punctuation]
  puncremove=''.join(puncremove)
  stopwords=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
  return [word for word in puncremove.split() if word.lower() not in stopwords]

app = Flask(__name__)
model=joblib.load("rforest.pkl")
def spampredict(message):
    x=[]
    x.append(message)
    if len(x[0])==0:
        return "The input is missing. Please input your sms and press predict."
    f=lambda x:x if x=='spam' else 'not spam'
    return f(model.predict(x)[0])

@app.route('/',methods=['GET','POST'])
def index():
    path="https://www.htmlcsscolor.com/preview/gallery/F5F5F5.png"#"https://www.macmillandictionary.com/external/slideshow/full/White_full.png"
    text=""
    if request.method == "POST":
        if len(request.form['test'])==0:
            text=spampredict(request.form['test'])
        else:
            if spampredict(request.form['test'])=='spam':
                path="https://media.giphy.com/media/Qx0zhgnni9e0g/giphy.gif"
                text="The message is "+spampredict(request.form['test'])
            else:
                text="The message is "+spampredict(request.form['test'])
                path="https://media.giphy.com/media/XIuGg4xhpz5uuD7wUr/giphy.gif"
        return render_template('index.html',path=path,data=text)
    return render_template('index.html',path=path,data=text)

if __name__ == '__main__':
    app.run(debug=True)
