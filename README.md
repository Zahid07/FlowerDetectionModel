# FlowerDetectionModel

A basic CNN model used to detect  the type of flower

The dataset was taken from kaggle



model_generation.ipynb:  Reads all the images from the respective folders. The images are then shuffled. Sklearn library is used to split dataset to train and test.
The train dataset then goes to the CNN model, which is later on saved.


Tkinter_Interface.py: A basic Tkinter front-end where the user uploads an image, and prediction is displayed.

Flask_Server.py: An end-point, which recieves the images, reads the saved model, and predicts the flower. Which then goes back to the front-end as a respones.
