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
acuarium ={}


print("name you acurium")

acuarium[input()]=liters 
print (acuarium)
print("you have fishes  or not |  yes/no")
if "no " or "" == input() :
	print ("how many fish have "); numbers_of_fishes=eval(input()) 
	fishes={}
	def wahtfish():
		name_of_fish= input( "waht is name of the fish:   ")
		long_of_fish = input("how many cm have the "+name_of_fish+":      ")
		fishes[name_of_fish]=long_of_fish	
	cero = 0
	while numbers_of_fishes> cero :
		whatfish=wahtfish()
		cero +=1
print(fishes)	