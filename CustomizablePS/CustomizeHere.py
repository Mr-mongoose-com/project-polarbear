# WARNING: Changing any code here will ALSO customize the gui_takepic_gather_photos.py file

# When setting these, MAKE SURE Bin3 IS A WIDE VARITY. (General Waste is always reccommended for Bin3. I would advise you to stick with General Waste if you don't know what you're doing)

# Set the three Bins here!
Bin1 = "Paper Recycling"
Bin2 = "Wood Recycling"
Bin3 = "General Waste"

# Set the minimum requirement for Bin1 or Bin2
MinReq = 30

# You will need to create a new AI Model,
# BUT, you can do this very easily with the gui_takepic_gather_photos.py (FOLLOW INSTRUCTIONS AT BOTTOM OF PAGE),
# which is ALSO on the github!

# Once you have A LOT of pictures, go to https://teachablemachine.withgoogle.com !

# Easily create TWO classes: Your first Bin, and you second Bin. (Bin1 was be the first class, and Bin2 must be the second)
# Then, train the model, and click 'export'

# Go to Tensorflow Lite, Click 'Floating Point', then click 'Download my Model'.

# When the model has downloaded, extract it to a location, and enter that location below

ModelPath = "/home/pi/Desktop/ModelForTFLite/model_floating.tflite" # Bear in mind that the file MUST BE INCLUDED! (e.g. /home/pi/Desktop/ModelForTFLite/model_floating.tflite)

# Don't worry if your model isn't called model_floating.tflite .

# As long as the model extension is .tflite , you're alright.








# FOR THE gui_takepic_gather_photos.py FILE

# Remember to, on your Raspberry Pi Desktop, create a folder called 'ImagesForTest' (No quotations)

# In that folder, create another folder, whith the EXACT SAME text as in the variable Bin1
# Repeat this for Bin2

# Now you can gather photos using gui_takepic_gather_photos.py!