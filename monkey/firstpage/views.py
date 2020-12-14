from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from tensorflow import Graph
import tensorflow as tf
# Create your views here.

img_height , img_width = 150,150
model_graph = Graph()
with model_graph.as_default():
    tf_session = tf.compat.v1.Session()
    with tf_session.as_default():
        model = load_model('./models/monkey_Xception.h5')


def home(request):
    return render(request,'home.html')

def predictResult(request):
    fileObj = request.FILES['Image']
    fs = FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    filePathName = fs.url(filePathName)
    testimage = '.'+filePathName
    img = image.load_img(testimage , target_size=(img_height,img_width))
    x = image.img_to_array(img)
    x = x/255
    x = x.reshape(1,img_height,img_width,3)
    with model_graph.as_default():
        with tf_session.as_default():
            predi = model.predict(x)
    p = list(predi[0])
    predictedLabel = p.index(max(p))
    common_name = ['Mantled Howler','Patas Monkey','Bald Uakari','Japanese Macaque','Pygmy Marmoset','White Headed Capuchin','Silvery Marmoset','Common Squirrel Monkey','Black Headed Night Monkey','Nilgiri Langur']
    latin_name = ['Alouatta Palliata','Erythrocebus Patas','Cacajao Calvus','Macaca Fuscata','Cebuella Pygmea','Cebus Capucinus','Mico Argentatus','Saimiri Sciureus','Aotus Nigriceps','Trachypithecus Johnii']
    cn = common_name[predictedLabel]
    ln = latin_name[predictedLabel]
    return render(request,'pred.html',{'cn':cn,'ln':ln})
