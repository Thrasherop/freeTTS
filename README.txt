This repo has a couple folders: compiled .exe file (which contains an 
easyish to use .exe version of the script), and the actual python source code.

USE:
When you run the file you will be prompted with some options. You can either just directly 
input the text you want to be read, or you can put 1, 2, or 3. The in.txt file is for 
pasting large chunks of text for TTS generation. If you press 2 to open it, the program
will freeze until you close the text editor window. Idk why but idc about fixing it cause
nobody is ever actually going to use it :) idek why I'm writting a README tbh


NOTE: Long text inputs can take awhile to generate. For example, 4-5 pages of 
text took maybe 10 minutes, but it made it a lot easier to read, so for me
it was the faster option. 


FILE TREE:
When the program is ran (either as a .py or .exe) it creates some files and folders 
(seen below). I recommend having a dedicated folder for the program and its dependancies,
then creating a shortcut (if you use it often).

./thisTTS (this file is temporary and should be deleted after the generation is done)

./mp3 (folder):
	in.txt (a file to paste large chunks of text. I.e. a whole chapter of an online book)
	thisTTS.mp3 (the actual audio of the last TTS generated)