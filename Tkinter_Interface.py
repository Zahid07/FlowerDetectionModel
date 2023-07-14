# create a simple tkinter interface which would take a picture and send it to the api

from tkinter import *
from tkinter import filedialog
import requests
import cv2
import numpy as np
from PIL import Image, ImageTk

root = Tk()
root.title('Flower Classification')
root.geometry('550x700')

# create a function to open the file dialog
def open_file():
    global img
    # global img_label
    global prediction_label
    
    # open the file dialog
    file = filedialog.askopenfilename(initialdir='/', title='Select a file', filetypes=(('jpg files', '*.jpg'), ('all files', '*.*')))

#    replace the image
    imgChosen = Image.open(file)
    imgChosen = imgChosen.resize((450, 330), Image.LANCZOS)
    imgChosen = ImageTk.PhotoImage(imgChosen)

    # create a label to show the image
    img_label = Label(image_frame, image=imgChosen)
    img_label.grid(row=0, column=0, padx=10, pady=10)

    # get the prediction
    getPrediction(file)


def getPrediction(file):
    
    # read the image
    img = cv2.imread(file)
    
    # resize the image
    img = cv2.resize(img, (64, 64))
    
    # convert the image to array
    img = np.reshape(img, [1, 64, 64, 3])

    # predict the image
    prediction = requests.post('http://localhost:5000/saveImage', files={'image': open(file, 'rb')})

    # set the prediction text
    prediction_text.delete(1.0, END)
    prediction_text.insert(END, prediction.text)



# create 2 frames top and bottom
top_frame = Frame(root, bg='white', width=480, height=50, highlightbackground='black', highlightthickness=1)
top_frame.grid(row=0, column=0, padx=10, pady=10)

# add 3 frames in the top frame
left_frame = Frame(top_frame, bg='white', width=150, height=50, highlightbackground='black', highlightthickness=1)
left_frame.grid(row=0, column=0, padx=10, pady=10)

center_frame = Frame(top_frame, bg='white', width=150, height=50, highlightbackground='black', highlightthickness=1)
center_frame.grid(row=0, column=1, padx=10, pady=10)

# add a button in the center frame
open_button = Button(center_frame, text='Open', command=open_file)
open_button.grid(row=0, column=0, padx=10, pady=10)

right_frame = Frame(top_frame, bg='white', width=150, height=50, highlightbackground='black', highlightthickness=1)
right_frame.grid(row=0, column=2, padx=10, pady=10)

# create a bottom frame
bottom_frame = Frame(root, bg='white', width=480, height=400, highlightbackground='black', highlightthickness=1)
bottom_frame.grid(row=1, column=0, padx=10, pady=10)
# add propagte false
bottom_frame.propagate(False)

# create 2 frames in the bottom frame top and bottom
bottom_top_frame = Frame(bottom_frame, bg='white', width=460, height=50, highlightbackground='black', highlightthickness=1)
bottom_top_frame.grid(row=0, column=0, padx=10, pady=10)

# add a label prediction
prediction_label = Label(bottom_top_frame, text='Prediction: ')
prediction_label.grid(row=0, column=0, padx=10, pady=10)

# add a prediction text
prediction_text = Text(bottom_top_frame, width=20, height=1)
prediction_text.grid(row=0, column=1, padx=10, pady=10)
# initialize with waiting
prediction_text.insert(END, 'Waiting...')

bottom_bottom_frame = Frame(bottom_frame, bg='white', width=460, height=340, highlightbackground='black', highlightthickness=1)
bottom_bottom_frame.grid(row=1, column=0, padx=10, pady=10)

# add a frame in the bottom bottom frame
image_frame = Frame(bottom_bottom_frame, bg='white', width=450, height=330, highlightbackground='black', highlightthickness=1)
image_frame.grid(row=0, column=0, padx=10, pady=10)
# add propagate false
image_frame.propagate(False)

imgChosen = Image.open('image.jpg')
imgChosen = imgChosen.resize((450, 330), Image.ANTIALIAS)
imgChosen = ImageTk.PhotoImage(imgChosen)

# create a label to show the image
img_label = Label(image_frame, image=imgChosen)
img_label.grid(row=0, column=0, padx=10, pady=10)






root.mainloop()

# run the api


