def surface(r,h):

sarea=((2*3.14*r*h)+(2*3.14* (r*r)))

print("Surface Area is ",sarea)

def volume(r,h):

volume=(3,14*(r*r)*h)

print("volume is", volume)

r=int(input("enter the radius: "))

h=int(input("enter the height: "))

while True:

print("1. Volume")

print("2.Surface Area")

print("3.Exit")

c=int(input("enter the choice: "))

if(c==1):

volume(r,h)

elif(c==2):

surface(r,h)

elif(c==3):

break

else:

print("invalid choice")
