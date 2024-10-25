from classes_new.endgame import endGamePoint
from classes_new.scoreread import ScoreRead
import json

# sets the constractors for the end game recdnisens and the score read
point = endGamePoint()
scoreread = ScoreRead()

# open a json file with all the data you want to save outside the code (for saveing points)
with open('pos.json', 'r') as json_file:
    data = json.load(json_file)

# function that input the data from the user while showing them what point they chainging
def enter_value(data,kay):
   data[kay] = int(input(f"{kay} = {data[kay]} : to setup enter a intger value\n"))

# do the same as the pravese function but with 2 inputs for x and y change an the same time
def enter_x_y_value(data,kay1,kay2):
   data[kay1] = int(input(f"{kay1} = {data[str(kay1)]} : to setup enter a intger value\n"))
   data[kay2] = int(input(f"{kay2} = {data[str(kay2)]} : to setup enter a intger value\n"))

# showing the points, get the new points and saveing tham and repet in loop
def set_data(data,x,y):
    while True:
        length = int(input("enter show length in seconds"))
        point.show_plases(length,data[str(x)],data[str(y)])
        enter_x_y_value(data,x,y)
        with open('pos.json', 'w') as file:
            json.dump(data, file)
        point.show_plases(length,data[str(x)],data[str(y)])
        if input("type 'exit' to exit") == "exit":
            break
# same as the pravese function but with one point (x or y)
def set_data_one(data,x):
    while True:
        length = int(input("enter show length in seconds"))
        point.show_plases(length,data[str(x)],data["y"])
        enter_value(data,x)        
        with open('pos.json', 'w') as file:
            json.dump(data, file)
        point.show_plases(length,data[str(x)],data["y"])
        if input("type 'exit' to exit") == "exit":
            break
# set the values for the score read
def set_score_Read(data,x,y):
        while True:
            scoreread.showimg()
            print("press q to exit the img window")
            enter_x_y_value(data,x,y)
            with open('pos.json', 'w') as file:
                json.dump(data, file)
            if input("type 'exit' to exit") == "exit":
                break

input("press enter to start setin")
# call all the functions 
set_data(data,"main_x","main_y")
set_data(data,"x","y")
set_data_one(data,"point_2_x")
set_data_one(data,"point_3_x")
set_score_Read(data,"read_x_1","read_y_1")
set_score_Read(data,"read_x_2","read_y_2")


