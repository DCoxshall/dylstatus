# dylstatus
## A customised replacement for i3status
I've recently been introduced to Arch Linux and i3wm, and I decided a fun
personal project would be to write a customised status bar from scratch.

This project was _heavily_ inspired by
[this](https://git.tdpain.net/codemicro/bar) project, a similar customised
i3status replacement written by a friend. I highly recommend checking it out,
mostly because her project is actually usable.

If you decide you want to try this on your machine (not recommended) then the
current setup is to simply clone the repo and put it somewhere you'll remember.
Then change the line `status_command i3status` to `status_command 
[your/path/to/main.py]` in your i3 config file (should be at the bottom). i3bar
can be reloaded by running `i3-msg reload`. 

Current modules:
- Date and time
- Internet connectivity
- Battery percentage and remaining time, with support for multiple batteries

dylstatus is currently still under development. Please be gentle.

