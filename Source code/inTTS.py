#COPYRIGHT github.com/Thrasherop

#Do what you want with this code though
#Idrc as long as it doesn't harm me.
#Its open source so change or distribute
#as desired

#Give me credit if you're distributing it and 
#if its convenient or easy.
#Credit isn't worth a bunch of effort
#So if its a pain don't worry about it bro

#Half the code isn't even mine in the first place lol


from gtts import gTTS
from playsound import playsound
import os 

print("Opening") 
  
def main():


	if not (os.path.exists("./mp3/in.txt")):
		os.system("echo foo > ./mp3/in.txt")


	mytext = input("\n\n\n\n\nPut 1 to read in.txt \nPut 2 to open in.txt for editing \nPut 3 to open previous TTS audio \nOtherwise, Input the text to read\n\n$ ")

	if mytext == "1":
		f = open("./mp3/in.txt", "r", encoding="utf8")
		mytext = f.read()
		f.close()
	elif mytext == "2":
		os.system("notepad ./mp3/in.txt")
		return
	elif mytext == "3":
		os.system("start ./mp3/thisTTS.mp3")
		return
	

	language = 'en'
	# Passing the text and language to the engine,  
	# here we have marked slow=False. Which tells  
	# the module that the converted audio should  
	# have a high speed 

	myobj = gTTS(text=mytext, lang=language, slow=False) 

	# Saving the converted audio in a mp3 file named 
	# welcome  

	if not (os.path.exists("./mp3")):
		os.system("mkdir mp3")


	myobj.save("thisTTS.mp3") 

	os.system("move thisTTS.mp3 ./mp3/")

	os.system("start ./mp3/thisTTS.mp3")


#playsound("thisTTS,mp3")

# Playing the converted file 
#os.system("mpg321 welcome.mp3")

while True:
	try:
		main()
	except Exception as e:
		#traceback.print_exc()
		print("Process failed: ", e)
		pass