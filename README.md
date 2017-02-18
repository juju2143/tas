# TAS

This repository contains Python scripts and a library I wrote designed to act as tool-assisted speedrun (TAS) movie files for PC games, that is, they automatically open a particular PC game, wait for the window to show up and send keypresses in order to complete them as fast as possible.

Of course, since it only sends keypresses and does not ensure the state is the same each time the movie is replayed (unlike Hourglass), the movies produced by this software are unlikely to be accepted on TASVideos.org, and are also extremely prone to desyncs.
Also, there is currently no way to record gameplay (although it should be possible). There is also no way to use savestates and the like.
So you have to edit the movie file manually and replay it from start each time. Quite cumbersome, I know, but it works. The concept of "rerecords" might not be applicable here, either.
For a real, state-of-the-art TAS, you might want to use Hourglass instead, although my scripts can be useful if you want to make a TAS of a simple game Hourglass does not support yet.
Likewise, you can't submit these runs on any sort of speedrun community as they usually won't allow TASing and speedruns done with scripts and will in no way be considered world records there.
I am not aware of any community that accepts TAS done with scripts such as this, but that would be nice.

I initially started this project in AppleScript, it's a pretty powerful language for automation, but the key up/key down functions were lacking in functionality, so I ported it in Python with Quartz.CoreGraphics, which is much more powerful.
There's still a bit of AppleScript left in there so it waits until the window shows up before starting the movie.

## Library

I'm aware there's a ton of libraries and software out there to automate keypresses and mouse actions, but this one is specifically designed for TASing, with the movie files supposed to look like, well, movie files, with all the keypresses and timing.
This only works on macOS, but support of other OSes such as Windows and Linux can be added later.

It contains a few useful functions pertaining to keypresses, mouse actions, opening software and waiting until the window show up, enough to make a good TAS.
More functions will be added as they will be deemed useful.

The library is found in `taslib.py`, you will find the documentation in the [wiki](https://github.com/juju2143/tas/wiki).
You will need [PyObjC](https://pypi.python.org/pypi/pyobjc-framework-Quartz) (usually installed by default on macOS) and [py-applescript](https://pypi.python.org/pypi/py-applescript) installed.

## Movie files

A good movie file should contain at least this header

```
#!/usr/bin/env python
from taslib import *
```

followed by a few comments (starting with `#`) with file information such as the name of the run, duration and information required in order to start the movie
(ex.: `# Game Name (version) "category, if applicable" by username in 13:37.42`) 
then a call to `openAndWait()` and the inputs. You can then run it with your python interpreter. You will find these scripts useful as examples.

### In progress

* `undertale.py` Undertale (v1.001) "hard mode" by juju2143

## Timing

Sure, you can derive the movie duration from the delay parameters, or measure the time with Python time functions, but I found an external timer such as [Llanfair](http://jenmaarai.com/llanfair/) particularly useful, especially if you're streaming on Twitch.
You can then assign F5 to start/split and F6 to reset in the config, then use `kPress("f5")` and `kPress("f6")` in your movie to automatically control the timer in your script, without any signifiant adverse effect to the timing.

## N64 Controller

Well, of course you can use the library for something else, like, I dunno [interfacing a Nintendo 64 controller](http://www.instructables.com/id/Use-an-Arduino-with-an-N64-controller/)? The `n64controller.py` script should work with this.

## Links

[Forum thread](https://codewalr.us/index.php?topic=1676.0)
