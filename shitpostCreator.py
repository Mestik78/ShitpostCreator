#
#	【B】【y】 【M】【e】【s】【t】【i】【k】【7】【8】
#	https://github.com/Mestik78

import random
from PIL import Image, ImageDraw, ImageFont
import glob

customWord = input("use custom word? [Y/N]: ")
if customWord == "Y" or customWord == "y":
	customWord = True

	word = input("word to use: ")
else:
	customWord = False

imagesNum = input("how many images? ")
print("creating " + str(imagesNum) + " images")

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

for x in range(0,int(imagesNum)):

	#importo las palabras:

	wordsFile = open('words.txt', 'r')
	words = wordsFile.readlines()
	wordsFile.close()

	with open('words.txt', 'r') as wordsFile:
		words = wordsFile.read().splitlines()


	#importo las imagenes:

	images = []
	for filename in glob.glob('images/*'): #assuming gif
		im=Image.open(filename)
		images.append(im)


	#elijo una palabra aleatoria

	if not customWord:
		word = words[random.randint(0, len(words)-1)].encode('latin1').decode('utf8')


	#elijo una imagen aleatoria

	image = images[random.randint(0, len(images)-1)]




	#pongo el texto en la imagen:

	font = ImageFont.truetype('impact.ttf', int(image.width / 10))

	draw = ImageDraw.Draw(image)

	w, h = draw.textsize(word, font = font)

	
	textX = (image.width-w)/2
	textY = (1 - 0.1) * image.height - h / 2

	# border
	textcolor = "white"
	shadowcolor = "black"

	shadowThickness = image.width / 300

	draw.text((textX-shadowThickness, textY-shadowThickness), word, font=font, fill=shadowcolor)
	draw.text((textX+shadowThickness, textY-shadowThickness), word, font=font, fill=shadowcolor)
	draw.text((textX-shadowThickness, textY+shadowThickness), word, font=font, fill=shadowcolor)
	draw.text((textX+shadowThickness, textY+shadowThickness), word, font=font, fill=shadowcolor)

	draw.text((textX,textY), word, font=font, fill=textcolor)

	#image.show()


	#cuantas veces se ha usado

	exports = []
	for filename in glob.glob('exports/*'):
		im=Image.open(filename)
		exports.append(im)


	#exporto la imagen
	image.save("exports/" + str(len(exports)) + ".png", "PNG")

	printProgressBar(x + 1, int(imagesNum), prefix = 'Progress:', suffix = 'Complete', length = 50)

print("done")
input()
exit()