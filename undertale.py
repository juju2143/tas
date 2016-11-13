#!/usr/bin/env python
from taslib import *
# Undertale (v1.001) "hard mode" by juju2143 in 0:56.76 (WIP)
# Instructions: The game should be fresh, without any saves.

fps=15.0
kPress("f6") # Reset timer
openAndWait("steam://run/391540", "UNDERTALE", "UNDERTALE")
kPress("f5") # Set timer
# Skip all the things
kPress("z",3)
kPress("z",1/fps,2)
# Name input
# Frisk (hard mode)
kPress("down",1/fps)
kPress("left",1/fps,2)
kPress("z",1/fps)
kPress("down",1/fps,5)
kPress("left",1/fps,2)
kPress("z",1/fps)
kPress("left",1/fps,2)
kPress("up",1/fps)
kPress("z",1/fps)
kPress("right",1/fps,3)
kPress("down",1/fps)
kPress("z",1/fps)
kPress("left",1/fps)
kPress("up",1/fps)
kPress("z",1/fps)
kPress("down",1/fps,3)
kPress("right",1/fps)
# Other names you can input (but they won't enable hard mode)
# Juju
#kPress("right",1/fps,2)
#kPress("down",1/fps)
#kPress("z",1/fps)
#kPress("left",1/fps,3)
#kPress("down",1/fps,5)
#kPress("z",1/fps)
#kPress("right",1/fps,3)
#kPress("up",1/fps,2)
#kPress("z",1/fps)
#kPress("left",1/fps,3)
#kPress("down",1/fps,2)
#kPress("z",1/fps)
#kPress("down",1/fps)
#kPress("right",1/fps)
# A (the fastest if you don't do hard mode)
#kPress("z",1/fps)
#kPress("up",1/fps)
#kPress("right",1/fps,2)
# Done
kPress("z",1/fps)
kPress("right",1/fps)
kPress("z",6.5)
# The adventure begins
kPress("f5")
kDown("down")
kDown("right",4/fps)
kUp("down",5)
kUp("right")
kDown("up",1)
# Talk to Flowey
kType("xz",1/fps,2)
kType("xz",1/fps,0,80)
kUp("up")
kDown("down")
kDown("left")
kType("xz",1/fps,0,170)
kUp("down")
kUp("left")
kPress("f5")
kHold("up",3)
kPress("f5")
