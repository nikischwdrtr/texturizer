from PIL import Image,ImageFont,ImageDraw
import glob,os,numpy,shutil,sys

#  start
# -------

print (" ")
print (" __________________________________________________")
print ("|       _/_/      _/_/_/    _/_/_/  _/_/_/  _/_/_/ |")
print ("|    _/    _/  _/        _/          _/      _/    |")
print ("|   _/_/_/_/    _/_/    _/          _/      _/     |")
print ("|  _/    _/        _/  _/          _/      _/      |")
print ("| _/    _/  _/_/_/      _/_/_/  _/_/_/  _/_/_/     |")
print ("|__________________________________________________|")
print ("|                                                  |")
print ("| ascii.py v0.1 2022                               |")
print ("| \ \ image to ascii art                           |")
print ("|                                                  |")
print ("|__________________________________________________|")
print ("|                                                  |")
print ("|           dev@niklausiff.ch                      |")
print ("|           https://www.niklausiff.rip             |")
print ("|__________________________________________________|")
print (" ")

#  settings
# ----------

# folder stuff
mydir = "./"
newdir = "ascii"
path = os.path.join(mydir,newdir)

# get list of files
jpg_list = glob.glob(mydir + "*.jpg")
jpgbig_list = glob.glob(mydir + "*.JPG")
png_list = glob.glob(mydir + "*.png")

# ascii array
ascii_chars = ['$','*','|','/','#','','','','']
# ascii_chars = ['$','*','|','/','#','£','X','','']

print (">>> 1/2 create folder")
print ("___________________________________________________")

# create folder
if os.path.exists(path):
  print (" ")
  print ("folder 'ascii' already exists. want to remove?")
  yn = input("> y/n: ")
  if yn == "y":
    shutil.rmtree(path)
  else:
    print ("___________________________________________________")
    print (" ")
    print (">>> 0/2 move folder and try again")
    sys.exit()
os.mkdir(path)

print (" ")
print (">>> 2/2 create image")
print ("___________________________________________________")

#  functions
# -----------

# ascii function
def ascii(image):
  img = Image.open(image)
  w_big, h_big = img.size
  smallIMG = img.resize((int(w_big/15), int(h_big/15)))
  img_matrix = numpy.array(smallIMG)
  w, h = smallIMG.size
  ascii_str = []
  for y in range(h):
    ascii_str.append("")
    for x in range(w):
      whichChar = mapArray(img_matrix[y][x],0,255,0,len(ascii_chars)-1)
      ascii_str[y] += ascii_chars[int(whichChar)]
  drawImage(ascii_str,image,w_big,h_big)

# draw image function
def drawImage(chars,image,w,h):
  asciiIMG = Image.new('RGBA', (w, h), color = (255,255,255,0))
  fnt = ImageFont.truetype("./CourierNew.ttf", 25)
  for y in range(int(h/15)):
    if y <= 0:
      ImageDraw.Draw(asciiIMG).text((0,0),chars[y],font=fnt,fill=(255,255,255))
    else:
      ImageDraw.Draw(asciiIMG).text((0,y*15),chars[y],font=fnt,fill=(255,255,255))
    # ImageDraw.Draw(asciiIMG).text((0,y+1),chars[y],font=fnt,fill=(0,0,0))
  asciiIMG.save(os.path.join(path+image[1:-4]+'.png'))

# map function
def mapArray(n, start1, stop1, start2, stop2):
  newval = (n - start1) / (stop1 - start1) * (stop2 - start2) + start2
  return newval

#  run functions
# ---------------

# ascii images
for x in range(len(jpg_list)):
  ascii(jpg_list[x])
for x in range(len(jpgbig_list)):
  ascii(jpgbig_list[x])
for x in range(len(png_list)):
  ascii(png_list[x])

print (" ")
print (" __________________________________________________")
print ("|                                                  |")
print ("| finished                                         |")
print ("|__________________________________________________|")
print ("|                                                  |")
print ("| ascii images:                                    |")
print ("| ./ascii                                          |")
print ("|__________________________________________________|")
print ("|                                                  |")
print ("|           dev@niklausiff.ch                      |")
print ("|           https://www.niklausiff.rip             |")
print ("|__________________________________________________|")
print (" ")