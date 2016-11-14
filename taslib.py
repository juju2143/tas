from time import sleep
from Quartz.CoreGraphics import *
from subprocess import call, Popen, PIPE
import applescript

debug = False

def debugMode(d):
	global debug
	debug = d
def dprint(str):
	global debug
	if debug:
		print(str)
def keyCodeFromString(keyString):
	keys = {"a": 0,"s": 1,"d": 2,"f": 3,"h": 4,
		"g": 5,"z": 6,"x": 7,"c": 8,"v": 9,
		"b": 11,"q": 12,"w": 13,"e": 14,"r": 15,
		"y": 16,"t": 17,"1": 18,"2": 19,"3": 20,
		"4": 21,"6": 22,"5": 23,"=": 24,"9": 25,
		"7": 26,"-": 27,"8": 28,"0": 29,"]": 30,
		"o": 31,"u": 32,"[": 33,"i": 34,"p": 35,
		"return": 36,"l": 37,"j": 38,"'": 39,"k": 40,
		";": 41,"\\": 42,",": 43,"/": 44,"n": 45,
		"m": 46,".": 47,"tab": 48," ": 49,"`": 50,
		"delete": 51,"enter": 52,"escape": 53,"np.": 65,"np*": 67,
		"np+": 69,"clear": 71,"np/": 75,"npenter": 76,"np-": 78,
		"np=": 81,"np0": 82,"np1": 83,"np2": 84,"np3": 85,
		"np4": 86,"np5": 87,"np6": 88,"np7": 89,"np8": 91,
		"np9": 92,"f5": 96,"f6": 97,"f7": 98,"f3": 99,
		"f8": 100,"f9": 101,"f11": 103,"f13": 105,"f14": 107,
		"f10": 109,"f12": 111,"f15": 113,"help": 114,"home": 115,
		"pgup": 116,"delete": 117,"f4": 118,"end": 119,"f2": 120,
		"pgdn": 121,"f1": 122,"left": 123,"right": 124,"down": 125,
		"up": 126,
	}
	return keys[keyString]
def openAndWait(app, process, window):
	call(["open",app])
	dprint(process + " opened, waiting for window...")
	scpt = '''
	on run {proc, win}
		tell application "System Events"
			repeat until window win of process proc exists
			end repeat
			set frontmost of process proc to true
		end tell
	end run
	'''
	#p = Popen(['osascript', '-', process, window], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	#stdout, stderr = p.communicate(scpt)
	applescript.AppleScript(scpt).run(process, window)
	dprint("done.")
def mEvent(type, posx, posy):
	theEvent = CGEventCreateMouseEvent(None, type, (posx,posy), kCGMouseButtonLeft)
	CGEventPost(kCGHIDEventTap, theEvent)
#	CFRelease(theEvent)
def mMove(posx, posy, delay=0):
	mEvent(kCGEventMouseMoved, posx, posy)
	dprint("mouse moved")
	sleep(delay)
def mDown(posx, posy, delay=0):
	mEvent(kCGEventLeftMouseDown, posx, posy)
	dprint("mouse down")
	sleep(delay)
def mUp(posx, posy, delay=0):
	mEvent(kCGEventLeftMouseUp, posx, posy)
	dprint("mouse up")
	sleep(delay)
def mClick(posx, posy, delay=0, reps=1):
	for i in range(0,reps):
		mDown(posx, posy)
		mUp(posx, posy)
		sleep(delay)
def mHold(posx, posy, delay=0, reps=1):
	for i in range(0,reps):
		mDown(posx, posy)
		sleep(delay)
		mUp(posx, posy)
def mCurPos():
	theEvent = CGEventCreate(None)
	return CGEventGetLocation(theEvent)
def mDownHere(delay=0):
	posx, posy = mCurPos()
	mDown(posx, posy, delay)
def mUpHere(delay=0):
	posx, posy = mCurPos()
	mUp(posx, posy, delay)
def mClickHere(delay=0, reps=1):
	posx, posy = mCurPos()
	mClick(posx, posy, delay, reps)
def mHoldHere(delay=0, reps=1):
	posx, posy = mCurPos()
	for i in range(0,reps):
		mDown(posx, posy)
		sleep(delay)
		mUp(posx, posy)
def kEvent(key, isDown):
	theEvent = CGEventCreateKeyboardEvent(None, key, isDown)
	CGEventPost(kCGHIDEventTap, theEvent)
#	CFRelease(theEvent)
def kDown(key, delay=0):
	code = keyCodeFromString(key)
	kEvent(code,True)
	dprint("key down")
	sleep(delay)
def kUp(key, delay=0):
	code = keyCodeFromString(key)
	kEvent(code,False)
	dprint("key up")
	sleep(delay)
def kPress(key, delay=0, reps=1):
	for i in range(0,reps):
		kDown(key)
		kUp(key)
		sleep(delay)
def kHold(key, delay=0, reps=1):
	for i in range(0,reps):
		kDown(key)
		sleep(delay)
		kUp(key)
def kType(keys, delay=0, delay2=0, reps=1):
	for i in range(0,reps):
		for c in keys:
			kPress(c, delay)
		sleep(delay2)
def kHolds(keys, delay=0, reps=1):
	for i in range(0,reps):
		for c in keys:
			kDown(key)
		sleep(delay)
		for c in keys:
			kUp(key)
