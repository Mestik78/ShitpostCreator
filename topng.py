import glob
from PIL import Image

images = []
for filename in glob.glob('rawimages/*'): #assuming gif
	im=Image.open(filename)
	images.append(im)

for i in range(len(images)):
	images[i].save('images/' + str(i) + '.png', "PNG")