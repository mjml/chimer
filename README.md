Dependencies:

* PulseAudio (sink is selectable using the PULSE_SINK environment variable)
* VLC (uses command line interface)

You can run this script from .xsession or window manager auto-start. All these files
  go in $HOME/etc/chimer, but you could edit that in the script.

There's also a "period" variable in the script if you'd like to change the interval
  to say, 20 minutes. The default is 15.

There are four different sounds included. The default order is to cycle marimba notes
  from 1-4, then repeat the first until the next hour begins.

Enjoy!
