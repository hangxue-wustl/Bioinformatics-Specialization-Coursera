def convolutionList(Spectrum):
	l=len(Spectrum)
	List=[]
	for i in range (l):
		for j in range (i+1, l):
			d = Spectrum[j]-Spectrum[i]
			if d!=0:
				List.append(d)
	return List

if __name__ == "__main__":
	Spectrum=[0,137,186,323]
	print (convolutionList(Spectrum))