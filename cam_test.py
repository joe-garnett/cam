from picamera2 import Picamera2, Preview
import file_manager
import time
from os import path



picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start()

exit_flag = False

while not exit_flag: 
    score = input("Enter combined score: ")
    if score.lower() == "exit":
        exit_flag = True
    else:   
        filename = score + '.jpg'
        picam2.capture_file(path.join(".", "unsorted_image", filename))
        file_manager.add_image(filename)

picam2.stop()
picam2.close()