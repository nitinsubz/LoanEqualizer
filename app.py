
# coding: utf-8

# In[197]:


from flask import Flask, render_template,request
import numpy as np
import keras.models
import os

model = keras.models.load_model('LoanPredictionModelTh.h5')

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
    print(data)
    data.insert(9,0)

    data=np.array([data])
    
    #print(str(rawdata).count('1'))
    #print(rawdata)

    pred=model.predict(data)[0][0]
    if pred>0.5:
        return str(1)
    else:
        return str(0)


# In[201]:


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

