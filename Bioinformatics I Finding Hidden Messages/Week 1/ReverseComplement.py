
def ReverseComplement(text):
	Complement=""
	for i in range (len(text)):
		if text[len(text)-i-1]=="A":
			Complement += "T"
		if text[len(text)-i-1]=="T":
			Complement += "A"
		if text[len(text)-i-1]=="G":
 			Complement += "C"
		if text[len(text)-i-1]=="C":
 			Complement += "G"
	return Complement 	
if __name__ == "__main__":
	text= open('ReverseComplement.txt', 'r').read()
	print (ReverseComplement(text))
		