from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
from werkzeug.utils import secure_filename


# Keras
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer


app=Flask(__name__)
model_path='model1.h5'
model=load_model(model_path)

def model_predict(path,model):
    x=image.load_img(path,target_size=(150,150))
    x=image.img_to_array(x)
    x=np.expand_dims(x,axis=0)
    pred=model.predict(x)
    pred=np.argmax(pred,axis=1)
    if pred==0:
        pred='Its an Audi'
    elif pred==1:
        pred=='Its a Lambo'
    elif pred==2:
        pred=='Its a Merc'
    return preds
@app.route('/')
def main():
    return render_template('index.html')
@app.route('/predict',methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f=request.files['file']
        base_path=os.path.dirname('__file__')
        file_path=os.path.join(base_path,'uploads',secure_filename(f.filename))
        f.save(file_path)
        
        preds=model_predict(file_path,model)
        results=preds
        return result
    
    return None

if __name__=='__main__':
 app.run()
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 