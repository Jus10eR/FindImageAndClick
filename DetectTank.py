import pyautogui
import cv2
import numpy

import glob
import time
import random
import math

import keyboard
import os

from threading import Thread

# Custom Variables
max_loop = -1
click_rate = numpy.array([0.1, 0.3]) #usally 150ms slower than expected - max speed 100ms
location_offset_range = 5
amount_clicks = 2
stop_on_image_not_found = False


def moveAndClick(x, y, duration, amount_clicks=1):
    # Move to the location and click for given duration
    start_time = time.time() * 1000
    pyautogui.moveTo(x, y, duration)    
            
    #left click
    for i in range(amount_clicks): 
        pyautogui.click()

    passed_time = time.time() * 1000 - start_time
    print(f"Clicked at ({x}, {y}) clicked {amount_clicks} times in {int(passed_time)} ms given duration was {int(duration*1000)} ms")

# search and click image in the center
def clickImage(image, threshold=0.7):

    # grab windows print screen
    screen_img = pyautogui.screenshot() 

    screen_img_rgb = numpy.array(screen_img)
    
    # convert screen img to grayscale
    screen_img_gray = cv2.cvtColor(screen_img_rgb, cv2.COLOR_BGR2GRAY) 
    
    # read image
    template = cv2.imread(image,cv2.IMREAD_GRAYSCALE)
    template.shape[::-1]

    # search for matching image in screen
    res = cv2.matchTemplate(screen_img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)    
    locations = numpy.where(res >= threshold)
    
    # no image is found 
    if max_val < threshold:
        print("No image is found")
        return -1
    
    # move mouse to image    
    index = 0
    for point in zip(*locations[::-1]):
        index += 1
        x, y = point
        
        location_offsets = numpy.array([random.randint(-location_offset_range, location_offset_range) for i in range(2)])
        click_duration = random.uniform(click_rate[0],  click_rate[1])
        final_x = x + template.shape[1]/2 + location_offsets[0]
        final_y = y + template.shape[0]/2 + location_offsets[1]

        if 'last_point' in vars() and last_point != None:
            last_x, last_y = last_point
            
            point_distance = pow(pow((last_x - x), 2) + pow((last_y - y), 2), 0.5)
            template_size = pow(pow(template.shape[0], 2) + pow(template.shape[1], 2), 0.5)
                        
            if point_distance < template_size:
                index -= 1
            else:
                moveAndClick(final_x, final_y, click_duration, amount_clicks)
        else:
            moveAndClick(final_x, final_y, click_duration, amount_clicks)    
            
        last_point = point

    return 0;    

#main thread
def main():
    loop = 0    
    time.sleep(1) 
    while loop != max_loop:
        # search images in input_images folder
        loop += 1
        for file in glob.glob("./input_images/*.png"):
            print("File: " + file + " Loop:  " + str(loop))            
            ret = clickImage(file)
            if (ret == -1 and stop_on_image_not_found):
                loop = max_loop
                break
    os._exit(0)    

#interrupt thread
def key_listener():
    if keyboard.read_key() == "esc":
        print("Interrupted")
        os._exit(0)
        
try:
    print("Press 'Escape' to quit this application anytime")

    thread1 = Thread(target = main)
    thread2 = Thread(target = key_listener)
    
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    
except:
    print ("Exiting")
    os._exit(0)


 
