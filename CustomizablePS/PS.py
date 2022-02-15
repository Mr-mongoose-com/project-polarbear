# This file is both the PGUI and the PAI.
# The advantage of this is that the files can interact with each other without importing anything
# Before I had an issue where the files tried to import from each other, AT THE SAME TIME
# As you probably guessed, this sucked, and failed.
# So here we are!

# You can also CUSTOMIZE this project with the CustomizeHere.py file!
# Have fun with that!

# To allow customization
from CustomizeHere import *



#     / / /         /\         /
#     /   /        /  \        /
#     / / /       /----\       /
#     /          /      \      /
#     /         /        \     /


import tensorflow as tf
import numpy as np

# Define Output Variable
Output = ""

def ActivateAI():
    # Load the model

    interpreter = tf.lite.Interpreter(model_path=ModelPath)
    interpreter.allocate_tensors()

    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Test model on random input data.
    input_shape = input_details[0]['shape']
    input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
    interpreter.set_tensor(input_details[0]['index'], input_data)

    interpreter.invoke()

    # The function `get_tensor()` returns a copy of the tensor data.
    # Use `tensor()` in order to get a pointer to the tensor.
    output_data = interpreter.get_tensor(output_details[0]['index'])

    # Set converter variable
    converter = output_data[0]

    # Set label1 and label2
    label1 = converter[0]
    label2 = converter[1]

    # Set variables for the console and maths
    PaperPercent = round(label1 * 100)
    WoodPercent = round(label2 * 100)

    print(f'''
    -------------------------------

    {Bin1} (label1): {PaperPercent}%                                                                     Real Number: {label1 * 100}%
    {Bin2} (label2): {WoodPercent}%                                                                      Real Number: {label2 * 100}%

    Final Output:
    ''')

    # Set Output to null and clear the AiPredictionMainText2 Text
    Output = ""
    AiPredictionMainText2.clear()

    if label1 > label2:

      if label1 > (MinReq / 100):
        Output = Bin1
      else:
        Output = Bin3

    elif label2 > label1:
        
      if label2 > (MinReq / 100):
        Output = Bin2
      else:
        Output = Bin3

    else:
      print("Error: No label is greater")

    if Output == Bin1:
      print(f"    {Bin1}\n")
    
    elif Output == Bin2:
      print(f"    {Bin2}\n")

    elif Output == Bin3:
      print(f"    {Bin3}\n")

    AiPredictionWindow.focus()
    AiPredictionMainText2.append(Output)



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
from os import system

# Defining variables to make it easier for me to code ;)
Wait = time.sleep
Time = time.time()
gui = guizero
TermCom = system
GetFont = truetype
PlayMusic = system

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

# ScanItemWindow creating and defining
ScanItemWindow = gui.Window(app, title="Scan an Item!")
ScanItemWindow.full_screen = "true"
ScanItemWindow.bg = "#00964b"
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

# Defing variables for the Home Page
def ScanItem():
  ScanItemWindow.focus()
  ScanItemPhotoTakenText.hide()
  ScanItemAiLoadingText.hide()

def HowToUse():
  HowToUseWindow.focus()

def ExitApp():
 app.destroy()

def BackToHomePage():
  app.focus()

def TakePhoto():
  TermCom("fswebcam -r 1280x720 --no-banner /home/pi/Desktop/paimage.jpeg")

def ShowAiLoading():
  AiLoadingWindow.focus()
  Wait(3)
  ActivateAI()

# New Line
gui.Text(app, text='''

''')

# Scan Item Buttons (Continue Button) defining
ScanItemButton = gui.PushButton(app, ScanItem, text="   Scan an Item   ")
ScanItemButton.bg = "red"
ScanItemButton.font = "ComicSansMS"
ScanItemButton.text_color = "#ffffff"

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
HowToUseWindowText = '''

Project PolarBear was created to encourage Pre-Prep pupils to recycle.

How it works:

The USB webcam (using fswebcam through tbe terminal) takes an image of
the object you wish to recycle, and feeds it to the Raspberry Pi with
Tensorflow 2.2.0. The Tensorflow Model compares your image to the images
stored on the SD Card. If it has over a 90% value of being identical,
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

# ScanItem Text
ScanItemText = gui.Text(ScanItemWindow, text="Scan an Item")
ScanItemText.text_color = "#ffffff"
ScanItemText.font = "ComicSansMS"
ScanItemText.text_size = "15"

gui.Text(ScanItemWindow, text='''

''')

# ScanItemWindow Take A Photo Button
ScanItemTakePhotoButton = gui.PushButton(ScanItemWindow, TakePhoto, text="Take A Photo")
ScanItemTakePhotoButton.bg = "red"
ScanItemTakePhotoButton.text_color = "#ffffff"
ScanItemTakePhotoButton.font = "ComicSansMS"

# ScanItemWindow Taken Photo Text
ScanItemPhotoTakenText = gui.Text(ScanItemWindow, text="Photo Taken!")
ScanItemPhotoTakenText.text_color = "#ffffff"
ScanItemPhotoTakenText.font = "ComicSansMS"
ScanItemPhotoTakenText.text_size = "11"
ScanItemPhotoTakenText.hide()

gui.Text(ScanItemWindow, text='''

''')

# ScanItemWindow Actiavte AI Button
ScanItemActivateAIButton = gui.PushButton(ScanItemWindow, ShowAiLoading, text="Activate AI")
ScanItemActivateAIButton.bg = "red"
ScanItemActivateAIButton.text_color = "#ffffff"
ScanItemActivateAIButton.font = "ComicSansMS"

# ScanItemWindow AI Loading Text
ScanItemAiLoadingText = gui.Text(ScanItemWindow, text="AI Loading...")
ScanItemAiLoadingText.text_color = "#ffffff"
ScanItemAiLoadingText.text_size = "11"
ScanItemAiLoadingText.font = "ComicSansMS"
ScanItemAiLoadingText.hide()

gui.Text(ScanItemWindow, text='''

''')

# ScanItemwindow Return Button
ScanItemReturnButton = gui.PushButton(ScanItemWindow, BackToHomePage, text="Return to Homepage")
ScanItemReturnButton.bg = "red"
ScanItemReturnButton.text_color = "#ffffff"
ScanItemReturnButton.font = "ComicSansMS"

# AiPredictionWindow Text
AiPredictionText = gui.Text(AiPredictionWindow, text="The AI Prediction!")
AiPredictionText.text_color = "#ffffff"
AiPredictionText.text_size = "25"
AiPredictionText.font = "ComicSansMS"

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

# Displays the app
app.full_screen = "true"
app.display()

# Neaten the console
print("\n    -------------------------------\n")