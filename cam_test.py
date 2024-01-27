from picamera2 import Picamera2, Preview
import file_manager
import time
import os



picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start()

exit_flag = False

while not exit_flag: 
    score = input("Enter score: ")
    if score.lower() == "exit":
        exit_flag = True
    elif score == "dirs":
        file_manager.create_master_files()
    else:   
        filename = score + '.jpg'
        picam2.capture_file(os.path.join(".", "unsorted_image", filename))

        picam2.capture_file(filename)
        os.rename(os.path.join(".", filename), os.path.join(".", "unsorted_image", filename))
        file_manager.add_image(filename)

picam2.stop()
picam2.close()