from fastapi import FastAPI,File,UploadFile
from tensorflow import keras
#import tensorflow as tf
##import uvicorn
import cv2
import numpy as np
#import  base64
#from PIL import Image
import io
app=FastAPI()

Filtered_breeds=['beagle', 'chihuahua', 'doberman','french_bulldog', 'golden_retriever', 'malamute', 'pug',
                 'saint_bernard', 'scottish_deerhound','tibetan_mastiff']

'''
def read_image(content):
    nparr=np.fromstring(content,np.uint8)
    image=cv2.imdecode(nparr,cv2.IMREAD_COLOR)
    image=cv2.resize(image,(312,312))
    image=np.array(image)
    return image

def load_model():
    model=keras.models.load_model('model.h5')
    return model

def predict(image,model):
    image=np.array([image])
    pred=model.predict(image)
    breed_index= np.argmax(pred)
    return {
        'breed ':Filtered_breeds[breed_index],
        'score ':str(pred[0][breed_index])
        }

'''
@app.get('/index')
async def hello_world():
    return "Hello world!"

@app.post("/predict/image")
async def predict_api():
    return "hossam"
#async def predict_api(file: UploadFile = File(...)):
 #   image=read_image(await file.read())
  #  model=load_model()
   # output=predict(image,model)
    #return output

#if __name__ =="__main__":
 #   uvicorn.run(app , port=8000 ,host='0.0.0.0')