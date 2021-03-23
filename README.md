# Monster Battle Dome
A simple monster dueling game

using python 3.8

By Nicholas Zehm (2013-1-8 original prototype)

Version 0.1.5 - Unstable
Experimental version

Changes (2021-3-23)
* GUI.py, MenuOptions.py for Tk interface

Version 0.1.4 (2021-3-19)
Stable Version

Changes:
* separated battle.py
* adjusted code to prevent circular referencing - now better suited for gui
* changed main, added interface and mainUserInterface to reduce printing of main_menu
* minor edits and fixes

Version 0.1.3.1 (2021-3-17)
Experimental version

Changes:
* Separated monster.py to minutely simplify code.
* Added stamina to the monster object
* Added level to the monster object
* updated with changes from version 0.1.1.2
* Adjusted the file date to reflect date of earliest prototype of this project (MonsterPenWorks.py)
* switched to international standard date format
* Adjust combat logic to utilize stamina
* Changed save system to save dictionary of objects
* Added a check for redundant names

Fixed:
* post battle healing logic fixed
* minor UI output stuff

ToDo:
* finish design of UI, teathering files and associated code
* adjust file structure
* finish function descriptions throughout code
* multiple pens to save file
* delete pens from save file
* save as?

* use an internal ID system for monsters, instead of name?
    -why do this?

* user interaction for attacks/defense
* leveling
* other monster attributes
