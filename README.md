#Mercedes MP3 card reader cmd script for COMAND & SD cards

##Problem
The Mercedes COMAND system has no media interface for reading from SD cards. It work fine when you attach a device with a media player (iPod, Android etc..) but not on a flat directory structure. This script writes a set of playlists and folders to make small collection available to COMAND.

##Requirements
- Python
- Command line access
- eye3d installed
- Writeable drives (non-corporate controlled)

##Assumptions
- That your source files are collected into Albums, iTunes does this on my windows machine.....
- Its only been tested on Windows 7 and Python 2.7
- Its looking for mp3 extensions
- Windows file system, '\' are hard coded

##Instructions
- Make sure python.exe is available in the $PATH
- execute python arg1 arg2-N
- ARG1= The drive letter of the SD card
- ARG2-N the folders with the music files

