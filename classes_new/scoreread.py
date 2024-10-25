# imports
import pyautogui
import cv2
import pytesseract
import numpy as np
import json

# class Score Read
class ScoreRead:

    # constractor
    def __init__(self):
        with open('pos.json', 'r') as json_file:
            data = json.load(json_file)
        self.left = min(data["read_x_1"],data["read_x_2"])
        self.top = min(data["read_y_1"], data["read_y_2"])
        self.width = abs(data["read_x_2"] - data["read_x_1"])
        self.height = abs(data["read_y_2"] - data["read_y_1"])
    # get a screen shot and extract the text using pytesseract engine
    def getscore(self):
        screenshot = pyautogui.screenshot()
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cropped_img = img[self.top:self.top+self.height, self.left:self.left+self.width]
        myconfig = r"--psm 6 --oem 3"
        text = pytesseract.image_to_string(cropped_img, config=myconfig)
        try:
            text = int(text)
        except ValueError:
            text = 0
        if text > 89999:
            text = text%10000
        return text
    
    # show the point the screen shot will be taken to extract the text
    def showimg(self):
        screenshot = pyautogui.screenshot()
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cropped_img = img[self.top:self.top+self.height, self.left:self.left+self.width]
        while True:
            key = cv2.waitKey(1)
            if key == ord('q'):
                cv2.destroyAllWindows()
                break
            cv2.imshow("Cropped Image", cropped_img)