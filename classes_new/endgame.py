import mss
import win32gui
import win32api
import time
import json


class endGamePoint:

    # set target color to 0
    color = (0,0,0)

    # constractor
    def __init__(self):
        pass

    # get a pixel color useing x and y
    def __get_pixel_color__(self, img, x,y):
        return img.pixel(x,y)
    
    # take data from the screen and returning true or false if you faild at the game
    def end_Game(self):
        with open('pos.json', 'r') as json_file:
            data = json.load(json_file)

        with mss.mss() as sct:
            monitor = {
                "top": data["main_y"] - data["y"],
                "left": data["main_x"] - data["x"],
                "width": data["x"]+1,
                "height": data["y"]+1
            }
            img = sct.grab(monitor)
            self.color = self.__get_pixel_color__(img,data["x"],0)
            point1 = self.__get_pixel_color__(img,data["x"],data["y"])
            point2 = self.__get_pixel_color__(img,data["point_2_x"],data["y"])
            point3 =  self.__get_pixel_color__(img,data["point_3_x"],data["y"])
            
            if point1 != self.color and point2 != self.color and point3 != self.color: return True
            return False        
    # drow a pixel on the screen
    def __draw_pixel__(self,x, y):
        colorq = (255,0,0)
        hdc = win32gui.GetDC(0)
        win32gui.SetPixel(hdc, x, y, win32api.RGB(*colorq))
        win32gui.ReleaseDC(0, hdc)
    
    # show the plase of the selected pixel for (input) amont of time
    def show_plases(self,time_to_run,x,y):
        r_time = time.time() + time_to_run
        while time.time() <= r_time:
            self.__draw_pixel__(x,y)
