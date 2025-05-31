# Counter-Strike-BunnyHop-Script-Open-Source
Advanced CS Bunny Hop Script (EDUCATIONAL PURPOSES ONLY!)


# Prerequisites

Windows OS

Python 3.7+ installed

Counter-Strike 1.6 running as hl.exe

Run PyCharm or Command Prompt as Administrator

Install Python Packages
Open PyCharm Terminal or Command Prompt and run:
```bash
pip install pymem keyboard pystray pillow
```
Run the Script in PyCharm

Paste the BunnyHop code into a Python file (e.g., bunnyhop.py)

Run the script with Admin privileges

Make sure CS 1.6 (hl.exe) is running

Press F1 to toggle BunnyHop on/off

Use tray icon to toggle or exit

Create Executable with PyInstaller

Install PyInstaller:
pip install pyinstaller

Create the executable:
```bash
pyinstaller bunnyhop.py --onefile
```

Find bunnyhop.exe inside the dist folder

Run the Executable

Run bunnyhop.exe as Administrator

Make sure CS 1.6 is running

Use F1 to toggle BunnyHop

Tray icon will reflect status

# Notes:

Always run script or exe as Administrator for memory access

Make sure game process name is hl.exe

Adjust jump delay in code if needed
