import random
import re
import math
import operator

"""This is the coding test from Comcast
Author: Peter Chao
Description: This program will generate a random coordinate between 1, 100 
             and arrange the given coordinates in an ascending order. 
"""

def main():

    x_orig,y_orig=random.randint(1,100),random.randint(1,100)
    new_dict={}
    coordinates =[
      {"id":"a","value":"1,49"},
      {"id":"b","value":"44,67"},
      {"id":"c","value":"93,6"},
      {"id":"d","value":"20,16"},
      {"id":"f","value":"71,8"},
      {"id":"g","value":"61,90"},
      {"id":"h","value":"34,97"},
      {"id":"i","value":"21,63"},
      {"id":"j","value":"19,84"},
      {"id":"k","value":"0,81"},
      {"id":"l","value":"6,76"},
      {"id":"m","value":"43,64"},
      {"id":"n","value":"18,64"},
      {"id":"o","value":"10,61"},
      {"id":"p","value":"37,27"},
      {"id":"q","value":"44,88"},
      {"id":"s","value":"99,46"},
      {"id":"t","value":"28,51"},
      {"id":"v","value":"47,21"},
      {"id":"w","value":"18,66"},
      {"id":"y","value":"75,92"},
      {"id":"z","value":"32,33"},
      {"id":"x","value":"84,100"},
      {"id":"r","value":"78,63"},
      {"id":"e","value":"68,53"},
      {"id":"u","value":"89,79"}
    ]
    for destination_coordinate in coordinates:
        key = (destination_coordinate["id"])
        x_destination,y_destination = re.split(',',(destination_coordinate["value"]))
        x_distance = x_orig-int(x_destination)
        y_distance = y_orig-int(y_destination)
        distance = round(math.sqrt(x_distance*x_distance+y_distance*y_distance),2)
        new_dict[key] = distance
    sorted_coordinates = sorted(new_dict.items(), key=operator.itemgetter(1))
    print ("The original coordinates = (%d, %d)"%(x_orig,y_orig))
    for coordinate in sorted_coordinates:
        print ("The next closest coordiante is:",coordinate)

if __name__== "__main__":
    main()

print ('Concluded!')
