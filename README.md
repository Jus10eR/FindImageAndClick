# FindImageAndClick
This is a simple auto clicker program written in Python that uses image recognition to find and click on a specified image on the screen. The program can be customized with various settings such as click rate, click amount, and stop on image not found.

## Requirements
Python 3.x
The following Python packages: pyautogui, cv2, numpy, keyboard, glob, threading
## Installation
Install the required Python packages by running the following command in the terminal:
```
pip install pyautogui opencv-python numpy keyboard
```
Save the provided code as a Python file, for example auto_clicker.py.
## Usage
Place the image files you want to click on in the input_images directory.

Customize the settings in the auto_clicker.py file, such as click rate, click amount, and stop on image not found.

Run the auto_clicker.py file in the terminal or command prompt:

```
python auto_clicker.py
```
The program will start clicking on the specified images with the configured settings. Press the 'Escape' key to quit the application at any time.
## Notes
* The program uses the pyautogui package to simulate mouse clicks, so make sure to test the program in a safe environment before using it on important *or sensitive applications.
* The program uses the cv2 package to perform image recognition, so make sure that the images you want to click on are clear and recognizable.
* The program uses the keyboard package to detect when the 'Escape' key is pressed to quit the application, so make sure that this package is installed and working correctly.
* The program uses the glob and threading packages to search for image files and run the program in separate threads, respectively.
