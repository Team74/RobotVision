import pixy
from ctypes import *
from pixy import *


class Tracker:

    blocks = BlockArray(100)
    
    def __init__(self):
        pixy.init()
    
    def trackSignature(self, _signature):
        print("Starting to track signature")
        pixy.change_prog("color_connected_components")
        print("Changed program to CCC")
        data = pixy.ccc_get_blocks(100, self.blocks)
        print("Data gathered")
        return data

    def trackColor(self, _x, _y):
        pixy.change_prog("video")
        return video_get_RGB(_x, _y)

    #Add logger capability

