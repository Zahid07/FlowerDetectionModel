# craete a simple Flask api which prints hello world
from flask import Flask
from flask import request
import os
import cv2
import numpy as np

app = Flask(__name__)

# load the model
from keras.models import load_model

model = load_model('image_classification_model.h5')

flower_types=[]

for folder in os.listdir('flowers'):
    flower_types.append(folder)

# create a route which would take a picture and save it in a folder
@app.route('/saveImage', methods=['POST'])
def save_image():
    # get the image from form
    # save the image in a folder
    img = request.files['image']
    
    # convert the image to array
    img = cv2.imdecode(np.fromstring(img.read(), np.uint8), cv2.IMREAD_UNCHANGED)   

    img = cv2.resize(img, (64, 64))
    img = np.reshape(img, [1, 64, 64, 3])

    # predict the image
    prediction = model.predict(img)
    prediction = np.argmax(prediction)
    prediction = flower_types[prediction]

    return prediction


if __name__ == "__main__":
    app.run(debug=True)
