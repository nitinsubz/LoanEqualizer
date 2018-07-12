
# coding: utf-8

# In[197]:


from flask import Flask, render_template,request
import numpy as np
import pickle
#import keras.models
import os
#from keras.models import model_from_json
#mport tensorflow as tf 
# Model reconstruction from JSON file
from sklearn.ensemble import RandomForestClassifier

with open('loantree.pkl','rb') as f:
    model=pickle.load(f)

#global graph
#graph = tf.get_default_graph()

# In[198]:


app = Flask(__name__)


# In[199]:


@app.route('/')
def index():
    #initModel()
    #render out pre-built HTML file right on the index page
    print("loaded website")
    return render_template("index.html")


# In[200]:


@app.route('/predict/',methods=['GET','POST'])
def predict():
    rawdata=request.get_data()
    data=[]

    temp=""
    add=False
    
    for s in str(rawdata):
        if s=="=":
            add=True
            continue
        if s=="&":
            add=False
            data.append(float(temp))
            temp=""
        if add:
            temp+=s

    data.append(float(temp[0:len(temp)-1]))
    data=[data]
    
    #print(str(rawdata).count('1'))
    #print(rawdata)
    
    #with graph.as_default():
    pred=model.predict_proba(data)[0]
    print(pred)
    if pred[0]>0.5:
        return str(0)
    return str(1)

# In[201]:


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

