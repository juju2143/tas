#!/usr/bin/python
import sys
import serial
from taslib import *

if len(sys.argv)<2:
    print("usage: "+sys.argv[0]+" tty")
    sys.exit()

deadZone = 4
mouseMode = False

#       A   B   Z   Str DU  DD  DL  DR  LRS ??? L   R   CU  CD  CL  CR
keys = ["z","x","v","c","w","s","a","d","c",".","q","e","i","k","j","l"]

#onUp = [lambda: None for i in range(0,16)]
#onDown = [lambda: None for i in range(0,16)]

onUp = [lambda: kUp(keys[i]) for i in range(0,16)]
onDown = [lambda: kDown(keys[i]) for i in range(0,16)]

#for i in range(0,2):
#    onUp[i] = lambda: mUp(x,y,0,i)
#    onDown[i] = lambda: mDown(x,y,0,i)

with serial.Serial(sys.argv[1], 115200) as ser:
    print("controller connected on "+sys.argv[1])
    obtns = [map(bool,map(int,x)) for x in ("0"*16).split()][0]
    while ser.is_open:
        line = ser.readline().strip()
        btns, sx, sy = line.split(" ")
	btns = [map(bool,map(int,x)) for x in btns.split()][0]
        sx, sy = [int(sx), int(sy)]
        if mouseMode:
            posx, posy = mCurPos()
            x, y = [posx+sx, posy-sy]
            if isPointVisible(x,y):
                mMove(x,y)
        else:
            if sx<-deadZone:
                kUp("right")
                kDown("left")
            elif sx>deadZone:
                kUp("left")
                kDown("right")
            else:
                kUp("left")
                kUp("right")
            if sy<-deadZone:
                kUp("up")
                kDown("down")
            elif sy>deadZone:
                kUp("down")
                kDown("up")
            else:
                kUp("down")
                kUp("up")
        for i in range(0,16):
            if btns[i]!=obtns[i]:
                if btns[i]:
                    print("btn "+str(i)+" pressed")
                    onDown[i]()
                else:
                    print("btn "+str(i)+" released")
                    onUp[i]()
	obtns = btns[:]
