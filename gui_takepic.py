# This code was for making an prototype and gatheing the picures of rubbish to train the PAI.

import guizero
import picamera
import time
from os import mkdir
from os.path import join

# Previous code that I ws going to use, but didn't

#directory = "PaperRecycling " + str(time.time())
#path = os.path.join(pardir, directory)
#mkdir(path)

# Defining variables which I use later on

Wait = time.sleep
gui = guizero
camera = picamera.PiCamera()
repeatWood = 0

# Setting camera resolution
camera.resolution = (896,896)

# Defing Function
def TakePicPaper():
    Wait(2)
    
    # Directory Variables
    pardirPaper = "/home/pi/Desktop/ImagesForTest/PaperRecycling"
    maindirPaper = str(time.time())
    
    # Joining them together
    pathPaper = join(pardirPaper, maindirPaper)
    # Making anothe directory
    mkdir(pathPaper)
    
    # Defining MORE VARIABLES
    repeatPaper = 0
    whilepathPaper = pathPaper + "/" + maindirPaper
    
    # Repeating it 50 times
    while repeatPaper < 50:
      
        # Taking a picture as a jpeg
        camera.capture(whilepathPaper + str(time.time()) + ".jpeg")
        repeatPaper += 1

def TakePicWood():
    Wait(2)
    
    # Same as function before
    pardirWood = "/home/pi/Desktop/ImagesForTest/WoodRecycling"
    maindirWood = str(time.time())
    pathWood = join(pardirWood, maindirWood)
    mkdir(pathWood)

    repeatWood = 0
    whilepathWood = pathWood + "/" + maindirWood

    while repeatWood < 50:
        camera.capture(whilepathWood + str(time.time()) + ".jpeg")
        repeatWood += 1

def TakePicGeneral():
    # I genuinely couldn't think of anything to do here
    print("haha dolfin lol")
    
# Defining the app var
app = gui.App(title="Take a video!")
# Text creation
message = gui.Text(app, text="Take a video of rubbish! Yaya!")
app.bg = "#00964b"

# Creating button
buttonPaper = gui.PushButton(app, TakePicPaper, text="Take a video of Paper Recycling!", height=3)
buttonWood = gui.PushButton(app, TakePicWood, text="Take a video of Wood Recycling!", height=3)
buttonGeneral = gui.PushButton(app, TakePicGeneral, text="Take a video of General Waste!", height=3)

# Button Background Colours
buttonGeneral.bg = "red"
buttonPaper.bg = "red"
buttonWood.bg = "red"

#Button Text sizes
buttonGeneral.text_size = 20
buttonPaper.text_size = 20
buttonWood.text_size = 20

# More text
gui.Text(app, text="After pressing a button, please hold still for 5s.", size=30)
gui.Text(app, text='''

''')

# Defining a funny meme
meme = gui.Picture(app, image="/home/pi/Desktop/ImagesForTest/tony-stark-bin-meme.jpeg")
meme.show()

#Displays the app
app.display()

# Closes the camera after the window of the gui has been closed
camera.close()
