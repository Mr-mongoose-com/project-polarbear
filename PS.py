# This file is both the PGUI and the PAI.
# The advantage of this is that the files can interact with each other without importing anything
# Before I had an issue where the files tried to import from each other, AT THE SAME TIME
# As you probably guessed, this sucked, and failed.
# So here we are!



# To neaten the console and to take a picture using fswebcam
from os import system
system("clear")
# If system("clear") is ever used, it's because the console is being neatened


# Hardware setting variables and servos
# ---------- Hardware start ----------
system("sudo pigpiod")

# Get rid of the errors (They don't mean anything)
system("clear")

from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

ServoFactory = PiGPIOFactory()

# Define Servos
PaperRecyclingServo = Servo(26, pin_factory=ServoFactory)     # Servo attached to GPIO Pin 26
WoodServo = Servo(6, pin_factory=ServoFactory)                # Servo attached to GPIO Pin 6
GeneralWateServo = Servo(5, pin_factory=ServoFactory)         # Servo attached to GPIO Pin 5

# Set all the bins to closed (max = closed, min = open)
PaperRecyclingServo.max()
WoodServo.max()
GeneralWateServo.max()

def ServoWaitNotSleep_PaperAndGeneral():
  TimerForServoWaitNotSleep = 0

  while TimerForServoWaitNotSleep < 100:
    TimerForServoWaitNotSleep += 1

def ServoWaitNotSleep_Wood():
  TimerForServoWaitNotSleepWood = 0

  while TimerForServoWaitNotSleepWood < 200:
    TimerForServoWaitNotSleepWood += 1

def ServoBin1():
  # Paper
  PaperRecyclingServo.min()
  #ServoWaitNotSleep_PaperAndGeneral()
  sleep(4)
  PaperRecyclingServo.max()

def ServoBin2():
  # Wood and Timber 
  WoodServo.min()
  #ServoWaitNotSleep_Wood()
  sleep(4)
  WoodServo.max()

def ServoBin3():
  # General Waste
  GeneralWateServo.min()
  #ServoWaitNotSleep_PaperAndGeneral()
  sleep(4)
  GeneralWateServo.max()
# ---------- Hardware end ----------



#     / / /         /\         /
#     /   /        /  \        /
#     / / /       /----\       /
#     /          /      \      /
#     /         /        \     /



import tensorflow.keras as tf
from PIL import Image, ImageOps
import numpy as np
import os

# Define Output Variable
Output = ""

# ---------- Pre-load Model Start ----------
print("Loading model...")

# Load the model

# Get's the Desktop path of most OS's. e.g. /home/pi/Desktop is now set to DesktopPath
DesktopPath = os.path.dirname(os.path.realpath(__file__))

model_path = f"{DesktopPath}/KerasModel/model.savedmodel"
model = tf.models.load_model(model_path, custom_objects=None, compile=True)

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# ---------- Pre-load Model End ----------

system("clear")

def ActivateAI(Model, Data):

    # Replace this with the path to your image
    img_filepath = "/home/pi/Desktop/paimage.jpeg" # Why are you readig this?
    image = Image.open(img_filepath)

    # Resize the image to a 224x224 with the same strategy as in TM2:
    # Resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # Turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    Data[0] = normalized_image_array

    # Run the inference
    prediction1 = Model.predict(Data)
    prediction2 = prediction1[0]

    label1 = prediction2[0]
    label2 = prediction2[1]

    print(f'''
    -------------------------------

    Paper Recycling (label1): {round(label1 * 100)}%                                                                     Real Number: {label1 * 100}%
    Wood Recycling (label2): {round(label2 * 100)}%                                                                       Real Number: {label2 * 100}%

    Final Output:
    ''')

    # Set Output to null and clear the AiPredictionMainText2 Text
    Output = ""
    AiPredictionMainText2.clear()

    # Define MinReq variable (Decimal)
    MinReq = 0.95

    if label1 > label2:

      if label1 > MinReq:
        Output = "Paper Recycling"
      else:
        Output = "General Waste"

    elif label2 > label1:
        
      if label2 > MinReq:
        Output = "Wood Recycling"
      else:
        Output = "General Waste"

    else:
      print("Error")

    if Output == 'Paper Recycling':
      print("    Paper Recycling\n")
    
    elif Output == 'Wood Recycling':
      print("    Wood Recycling\n")

    elif Output == 'General Waste':
      print("    General Waste\n")
   
    AiPredictionMainText2.append(Output)
    
    # Hardware
    if Output == 'Paper Recycling':
      ServoBin1()
    elif Output == 'Wood Recycling':
      ServoBin2()
    else:
      ServoBin3()

    AiPredictionWindow.focus()

# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /










#   / / /     / / /         /       /      /
#   /   /     /             /       /      /
#   / / /     /   / / /     /       /      /
#   /         /     /       /       /      /
#   /         / / / /       / / / / /      /

# Importing the four libries. PIL for loading fonts. GuiZero for (Obvs) making the gui. Time for a variable that costantly shifts and sleep. PiCamera didn't work so using fswebcam instead through terminal
from PIL.ImageFont import truetype
import guizero
import time

# Defining variables to make it easier for me to code ;)
Wait = time.sleep
Time = time.time()
gui = guizero
TermCom = system
GetFont = truetype

# Defining app background and app variables
app = gui.App(title="Project Polarbear")
app.bg = "#00964b"

# Defining local fonts accessed by PIL (Pillow)
ComicSansMS20 = GetFont("/home/pi/.fonts/ComicSansMS3.ttf", size=20)
ComicSansMS10 = GetFont("/home/pi/.fonts/ComicSansMS3.ttf", size=10)

# HowToUseWindow creating and defining
HowToUseWindow = gui.Window(app, title="How To Use")
HowToUseWindow.full_screen = "true"
HowToUseWindow.bg = "#00964b"
app.focus()

# TakingPhotoWindow creating and defining
TakingPhotoWindow = gui.Window(app, title="Taking a Photo..!")
TakingPhotoWindow.full_screen = "true"
TakingPhotoWindow.bg = "#00964b"
app.focus()

# AiPredictionWindow Creating and defining
AiPredictionWindow = gui.Window(app, title="AI Prediction")
AiPredictionWindow.full_screen = "true"
AiPredictionWindow.bg = "#00964b"
app.focus()

# AiLoadingWindow Creating and defining
AiLoadingWindow = gui.Window(app, title="AI Loading...")
AiLoadingWindow.full_screen = "true"
AiLoadingWindow.bg = "#00964b"
app.focus()

# Defing the Welcome Text
WelText = gui.Text(app, text="Welcome to Project Polarbear!", size="20")
WelText.text_color = "#ffffff"
WelText.font = "ComicSansMS"

def HowToUse():
  HowToUseWindow.focus()

def ExitApp():
 app.destroy()

def BackToHomePage():
  app.focus()

def TakePhoto(M, D):
  TakingPhotoWindow.focus()
  Wait(1.5)
  TermCom("fswebcam -r 1280x720 --no-banner /home/pi/Desktop/paimage.jpeg")
  ShowAiLoading(M, D)

def ShowAiLoading(Mod, Dat):
  AiLoadingWindow.focus()
  Wait(3)
  ActivateAI(Mod, Dat)

# New Line
gui.Text(app, text='''

''')

# Scan Item Buttons (Continue Button) defining
ScanItemButton = gui.PushButton(app, TakePhoto, args=[model, data], text="   Scan an Item   ")
ScanItemButton.bg = "red"
ScanItemButton.font = "ComicSansMS"
ScanItemButton.text_color = "#ffffff"
#ScanItemButton.text_size =

gui.Text(app, text='''

''')

# How to Use Button defining
HowToUseButton = gui.PushButton(app, HowToUse, text="About this Project")
HowToUseButton.bg = "red"
HowToUseButton.font = "ComicSansMS"
HowToUseButton.text_color = "#ffffff"

gui.Text(app, text='''

''')

# Exit Button Defining
ExitButton = gui.PushButton(app, ExitApp, text=" Exit the Project ")
ExitButton.bg = "red"
ExitButton.font = "ComicSansMS"
ExitButton.text_color = "#ffffff"

# HowToUseWindow Title Text
HowToUseTitleText = gui.Text(HowToUseWindow, text="About this Project")
HowToUseTitleText.text_color = "#ffffff"
HowToUseTitleText.font = "ComicSansMS"
HowToUseTitleText.text_size = "20"

# HowToUseWindow Main Text
HowToUseWindowText = f'''

Project PolarBear was created to encourage Pre-Prep pupils to recycle.

How it works:

The USB webcam (using fswebcam through tbe terminal) takes an image of
the object you wish to recycle, and feeds it to the Raspberry Pi with
Tensorflow 2.2.0. The Tensorflow Model compares your image to the images
stored on the SD Card. If it has over a 99% value of being identical,
the Model knows what object it is. It then sorts it into the correct
recycling bin and tells you what bin it should go in.
'''

HowToUseMainText = gui.Text(HowToUseWindow, text=HowToUseWindowText)
HowToUseMainText.text_color = "#ffffff"
HowToUseMainText.text_size = "15"
HowToUseMainText.font = "ComicSansMS"

# HowtoUseWindow Return Button
HowToUseReturnButton = gui.PushButton(HowToUseWindow, BackToHomePage, text="Return to Home Page")
HowToUseReturnButton.bg = "red"
HowToUseReturnButton.text_color = "#ffffff"
HowToUseReturnButton.font = "ComicSansMS"

# AiPreditionWindow Title
AiPredictionTitle = gui.Text(AiPredictionWindow, text="The AI Prediction!")
AiPredictionTitle.text_color = "#ffffff"
AiPredictionTitle.text_size = "20"
AiPredictionTitle.font = "ComicSansMS"

gui.Text(AiPredictionWindow, text='''

''')

# AiPrediction Main Text (Text split up into three sections, look at 3 variables below)
AiPredictionMainText1 = gui.Text(AiPredictionWindow, text="It should go in the...")
AiPredictionMainText2 = gui.Text(AiPredictionWindow, text=Output)
AiPredictionMainText3 = gui.Text(AiPredictionWindow, text="Bin!")

AiPredictionMainText1.text_color = "#ffffff"
AiPredictionMainText2.text_color = "#ffffff"
AiPredictionMainText3.text_color = "#ffffff"

AiPredictionMainText1.text_size = "15"
AiPredictionMainText2.text_size = "20"
AiPredictionMainText3.text_size = "15"

AiPredictionMainText1.font = "ComicSansMS"
AiPredictionMainText2.font = "ComicSansMS"
AiPredictionMainText3.font = "ComicSansMS"

gui.Text(AiPredictionWindow, text='''

''')

# AiPredictionWindow Return Button
AiPredictionGoToHomeButton = gui.PushButton(AiPredictionWindow, BackToHomePage, text="Return to Home Page")
AiPredictionGoToHomeButton.bg = "red"
AiPredictionGoToHomeButton.text_color = "#ffffff"
AiPredictionGoToHomeButton.font = "ComicSansMS"

# AiLoadingWindow moving Below text down
gui.Text(AiLoadingWindow, text='''


''')

# AiLoadingWindow Text
AiLoadingText = gui.Text(AiLoadingWindow, text="AI Loading...")
AiLoadingText.text_color = "#ffffff"
AiLoadingText.text_size = "35"
AiLoadingText.font = "ComicSansMS"

# TakingPhotoWindow moving Below text down
gui.Text(TakingPhotoWindow, text='''


''')

# TakingPhotoWindow Text
TakingPhotoText = gui.Text(TakingPhotoWindow, text="Taking a Photo...")
TakingPhotoText.text_color = "#ffffff"
TakingPhotoText.text_size = "35"
TakingPhotoText.font = "ComicSansMS"

system("clear")

# Displays the app
app.full_screen = "true"
app.display()

# Smarten the console
print("    -------------------------------")