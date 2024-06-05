#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


class Feladatok():
    def __init__(self):
        self.ev3 = EV3Brick()# tégla
        self.cs =ColorSensor(Port.S3)#szenzorok
        #self.ts =TouchSensor(Port.S1)
        #self.us =UltrasonicSensor(Port.S4)
        
    def okos_postalada(self):
        #ha valaki ki nyitja a postaládát akor meg változik a szin és jelezni hogy levél érkezett
        csukva_szin =self.cs.color()
        wait(1000)
        if(self.cs.color()!=csukva_szin):
            wait(1000)
            self.ev3.screen.print("Leveled érkezett!")
            #szine nem ani mint amugy akkor kuldon uzenetet különben nem
        wait(1000)

    def csipog(self):
        self.ev3.speaker.beep()

    