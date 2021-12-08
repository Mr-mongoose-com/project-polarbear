import tensorflow.keras as tf
from PIL import Image, ImageOps
import numpy as np
import os

# Load the model

# Get's the Desktop path of most OS's. e.g. /home/pi/Desktop is now set to DirectoryPath
DirectoryPath = os.path.dirname(os.path.realpath(__file__))

model_path = f"{DirectoryPath}/KerasModel"
model = tf.models.load_model(model_path, custom_objects=None, compile=True)

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
img_filepath = f"{DirectoryPath}/KerasModel/image2.jpeg"
image = Image.open(img_filepath)

#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
image_array = np.asarray(image)
# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
# Load the image into the array
data[0] = normalized_image_array

# run the inference
prediction1 = model.predict(data)
prediction2 = prediction1[0]

label1 = prediction2[0]
label2 = prediction2[1]

print(prediction2)

print(label1)
print(label2)

print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# Set an Output variable
Output = 0

if label1 > label2:
    Output = 'Box'
    #print("Box")
elif label2 > label1:
    Output = 'Flower'
    #print("Flower")
else:
    print("Error")

if Output == 'Box':
    print("Box")
elif Output == 'Flower':
    print("Flower")
