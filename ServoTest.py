# Open pigpiod
from os import system
system("sudo pigpiod")
# Rid of the error message (servo still works)
system("clear")

# Imports. gpiozero for interacting with the servos, time for the wait/sleep command and guizero for making the gui
from gpiozero import Servo
from time import sleep
import guizero

# Creating servo objects
from gpiozero.pins.pigpio import PiGPIOFactory

# Set variables to make it easier for me to code ;)
factory = PiGPIOFactory()
gui = guizero

# Define Servos
Paper_Recycling = Servo(26, pin_factory=factory)     # servos attached to gpio pin 26
Timber_and_Wood = Servo(5, pin_factory=factory)     # servos attached to gpio pin 5
General_Waste = Servo(6, pin_factory=factory)       # servos attached to gpio pin 6

# Set Bins to closed
Paper_Recycling.max()
Timber_and_Wood.max()
General_Waste.max()

def Bin1():
    # Paper
    Paper_Recycling.min()
    sleep(4)
    Paper_Recycling.max()

def Bin2():
    # Wood and Timber 
    Timber_and_Wood.min()
    sleep(4)
    Timber_and_Wood.max()

def Bin3():
    # General Waste
    General_Waste.min()
    sleep(4)
    General_Waste.max()

# Create/Set the app
app = gui.App(title="Charlie Weird thing")
app.bg = "#00964b"

# Text
Text = gui.Text(app, text="Open da bins!", size=15, color="white", font="ComicSansMS")

gui.Text(app, text='''

''')

# Create Bin1 Button
Bin1Button = gui.PushButton(app, Bin1, text="Open Paper Recycling")
Bin1Button.bg = "red"
Bin1Button.font = "ComicSansMS"
Bin1Button.text_color = "white"
Bin1Button.text_size = "12"

gui.Text(app, text='''

''')

# Create Bin2 Button
Bin2Button = gui.PushButton(app, Bin2, text="Open Wood Recycling")
Bin2Button.bg = "red"
Bin2Button.font = "ComicSansMS"
Bin2Button.text_color = "white"
Bin2Button.text_size = "12"

gui.Text(app, text='''

''')

# Create Bin3 Button
Bin3Button = gui.PushButton(app, Bin3, text="Open General Waste")
Bin3Button.bg = "red"
Bin3Button.font = "ComicSansMS"
Bin3Button.text_color = "white"
Bin3Button.text_size = "12"

# Set the app to full screen
app.full_screen = "true"

# Display the app
app.display()