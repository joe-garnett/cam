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
picam2.capture_file("test.jpg")