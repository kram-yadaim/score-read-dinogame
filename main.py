from classes_new.endgame import endGamePoint
from classes_new.scoreread import ScoreRead
import json
import csv
import os

# open json
with open('pos.json', 'r') as json_file:
    data = json.load(json_file)

# append data to csv function
def append_to_csv(file_name, number):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
    with open(file_path, mode='a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([number])
# sets end game points and score read constractor
point = endGamePoint()
scoreRead = ScoreRead()

flag = True
# loop for whan the game end read the score and save the result
while True:
    num = 0
    if not point.end_Game(): flag = True
    while flag:
        if point.end_Game():
            text = scoreRead.getscore()
            append_to_csv("data", text)
            flag = False
            print("end game")
