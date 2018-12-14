
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