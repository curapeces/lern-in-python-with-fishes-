print ("put the measurements of you fish tankin cm centimeters" )
print ("hegiht")
heigth =eval(input()) 
h = heigth  
print ("deep")
deep=eval(input()) 
d = deep
print ("large")
large= eval(input())
l = large

mileliters = d*l*h
liters = mileliters /1000

print ("liters of fish tank have ")
print(liters)

if d == h ==l:
	print ("you fish tank are cube ")
else :
	print ("you acurium are a rectangle ")

print ("and have in galons :")
galons = liters /3.73
print (galons)
