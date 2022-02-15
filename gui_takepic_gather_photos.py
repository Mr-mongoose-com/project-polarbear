
import guizero
import time
from os import mkdir
from os.path import join
from os import system

# Previous code that I ws going to use, but didn't

#directory = "PaperRecycling " + str(time.time())
#path = os.path.join(pardir, directory)
#mkdir(path)

Wait = time.sleep
gui = guizero
TermCom = system
repeatWood = 0

def TakePicPaper():
    Wait(2)
    
    pardirPaper = "/home/pi/Desktop/ImagesForTest/PaperRecycling"
    maindirPaper = str(time.time())
    pathPaper = join(pardirPaper, maindirPaper)
    mkdir(pathPaper)

    repeatPaper = 0
    whilepathPaper = pathPaper + "/" + maindirPaper

    while repeatPaper < 50:
        TermCom("fswebcam -r 1280x720 --no-banner " + whilepathPaper + str(time.time()) + ".jpeg")
        repeatPaper += 1

def TakePicWood():
    Wait(2)
    
    pardirWood = "/home/pi/Desktop/ImagesForTest/WoodRecycling"
    maindirWood = str(time.time())
    pathWood = join(pardirWood, maindirWood)
    mkdir(pathWood)

    repeatWood = 0
    whilepathWood = pathWood + "/" + maindirWood

    while repeatWood < 50:
        TermCom("fswebcam -r 1280x720 --no-banner " + whilepathWood + str(time.time()) + ".jpeg")
        repeatWood += 1

def TakePicGeneral():
    print("haha fin lol")

app = gui.App(title="Take a video!")
message = gui.Text(app, text="Take a video of rubbish! Yaya!", font="ComicSansMS")
app.bg = "#00964b"

gui.Text(app, text='''

''')

buttonPaper = gui.PushButton(app, TakePicPaper, text="Take a video of Paper Recycling!")

gui.Text(app, text='''

''')

buttonWood = gui.PushButton(app, TakePicWood, text="Take a video of Wood Recycling!")

gui.Text(app, text='''

''')

buttonGeneral = gui.PushButton(app, TakePicGeneral, text="Take a video of General Waste!")

# Button Background Colours
buttonGeneral.bg = "red"
buttonPaper.bg = "red"
buttonWood.bg = "red"

# Button Fonts
buttonGeneral.font = "ComicSansMS"
buttonPaper.font = "ComicSansMS"
buttonWood.font = "ComicSansMS"

#Button Text sizes
buttonGeneral.text_size = 10
buttonPaper.text_size = 10
buttonWood.text_size = 10

gui.Text(app, text='''

''')

gui.Text(app, text="After pressing a button, please hold still for 5s.", size=15, font="ComicSansMS")

#print(var1, var2, var3)

app.full_screen = "true"
app.display()