from picamera2 import Picamera2, Preview
import file_manager
import time
import os
import random

picam2 = Picamera2()
picam2.options["quality"] = 95
picam2.options["compress_level"] = 0
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
        brightness_factor = float(random.randrange(50,100)) / 100.0
        brightness_factors = [brightness_factor, 1.0]
        picam2.capture_file(filename)
        os.rename(os.path.join(".", filename), os.path.join(".", "unsorted_images", filename))
        for angle in range(0, 360, 15):
            for b in brightness_factors:
                file_manager.add_image(filename, angle, b)

picam2.stop()
picam2.close()