from PIL import Image
from itertools import product
import glob,os,numpy

print (" ")
print (" ____________________________________________________")
print ("| ▄▄▄▄▄▄▄▄ .▐▄• ▄ ▄▄▄▄▄▄• ▄▌▄▄▄  ▪  ·▄▄▄▄•▄▄▄ .▄▄▄   |")
print ("| •██  ▀▄.▀· █▌█▌▪•██  █▪██▌▀▄ █·██ ▪▀·.█▌▀▄.▀·▀▄ █· |")
print ("|  ▐█.▪▐▀▀▪▄ ·██·  ▐█.▪█▌▐█▌▐▀▀▄ ▐█·▄█▀▀▀•▐▀▀▪▄▐▀▀▄  |")
print ("|  ▐█▌·▐█▄▄▌▪▐█·█▌ ▐█▌·▐█▄█▌▐█•█▌▐█▌█▌▪▄█▀▐█▄▄▌▐█•█▌ |")
print ("|  ▀▀▀  ▀▀▀ •▀▀ ▀▀ ▀▀▀  ▀▀▀ .▀  ▀▀▀▀·▀▀▀ • ▀▀▀ .▀  ▀ |")
print ("|____________________________________________________|")
print ("|                                                    |")
print ("| texturizer.py v0.1 2022                            |")
print ("| \ \ texture algorithm                              |")
print ("|                                                    |")
print ("|____________________________________________________|")
print ("|                                                    |")
print ("|           dev@niklausiff.ch                        |")
print ("|           https://www.niklausiff.rip               |")
print ("|____________________________________________________|")
print (" ")

print (">>> 0/2 settings")
print ("_____________________________________________________")

# input settings
print (" ")
print ("emboss depth (0.0-100.0)")
dep = input("> value: ")

print ("_____________________________________________________")
print (" ")
print (">>> 1/2 create folder // get images")
print ("_____________________________________________________")

# folder stuff
mydir = "./"
newdir = "emboss"
path = os.path.join(mydir,newdir)

# get list of files
jpg_list = glob.glob(mydir + "*.jpg")
jpgbig_list = glob.glob(mydir + "*.JPG")
png_list = glob.glob(mydir + "*.png")

# create folder
os.mkdir(path)

print (" ")
print (">>> 2/2 emboss images")
print ("_____________________________________________________")

# defining azimuth, elevation, and depth
ele = numpy.pi/2.2 # radians
azi = numpy.pi/4.  # radians
dept = float(dep)

# emboss function
def emboss(image,ele,azi,dep):
  img = Image.open(image).convert('L') 
  a = numpy.asarray(img).astype('float')
  grad = numpy.gradient(a)
  grad_x, grad_y = grad
  gd = numpy.cos(ele)
  dx = gd*numpy.cos(azi)
  dy = gd*numpy.sin(azi)
  dz = numpy.sin(ele)
  grad_x = grad_x*dep/100.
  grad_y = grad_y*dep/100.
  leng = numpy.sqrt(grad_x**2 + grad_y**2 + 1.)
  uni_x = grad_x/leng
  uni_y = grad_y/leng
  uni_z = 1./leng
  a2 = 255*(dx*uni_x + dy*uni_y + dz*uni_z)
  a2 = a2.clip(0,255)
  img2 = Image.fromarray(a2.astype('uint8')) 
  img2.save(os.path.join(path+image[1:]))

# emboss images
for x in range(len(jpg_list)):
  emboss(jpg_list[x],ele,azi,dept)
for x in range(len(jpgbig_list)):
  emboss(jpgbig_list[x],ele,azi,dept)
for x in range(len(png_list)):
  emboss(png_list[x],ele,azi,dept)

print (" ")
print (" ____________________________________________________")
print ("|                                                    |")
print ("| finished                                           |")
print ("|____________________________________________________|")
print ("|                                                    |")
print ("| embossed images:                                   |")
print ("| ./emboss                                           |")
print ("|____________________________________________________|")
print ("|                                                    |")
print ("|           dev@niklausiff.ch                        |")
print ("|           https://www.niklausiff.rip               |")
print ("|____________________________________________________|")
print (" ")