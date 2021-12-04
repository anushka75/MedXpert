from django.shortcuts import render
from json.encoder import JSONEncoder
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from keras.models import load_model
from keras_preprocessing import image
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from rest_framework.views import APIView
import json
from django.core.files.storage import default_storage
import numpy as np
from tensorflow import Graph
import tensorflow as tf
from .serializer import FileSerializer

@csrf_exempt
def index(request):
    return render(request,"index.html")

img_height, img_width=224,224
with open('imagenet_classes.json','r') as f:
    labelInfo=f.read()
labelInfo=json.loads(labelInfo)

model_graph=Graph()
with model_graph.as_default():
    gpuoptions = tf.compat.v1.GPUOptions(allow_growth=True)
    tf_session = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(gpu_options=gpuoptions))
    with tf_session.as_default():
        model=load_model('best_model.h5')

@csrf_exempt
def covid(request):
    if request.method == "POST":
        file=request.FILES['imageFile']
        file_name=default_storage.save(file.name,file)
        file_url=default_storage.path(file_name)
        img=image.load_img(file_url,target_size=(img_height,img_width))
        x=image.img_to_array(img)
        x=x/255
        x=x.reshape(1,img_height,img_width,3)
        with model_graph.as_default():
            with tf_session.as_default():
                predi=model.predict(x)
        predictedLabel=labelInfo[str(np.argmax(predi[0]))]  
    return HttpResponse(predictedLabel)

# @api_view(['POST'])
# @parser_classes([FileUploadParser])
# def covid(request):
#     serializer=FileSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
