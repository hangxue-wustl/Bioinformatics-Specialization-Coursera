#Passed
def CodonTranslate(RNA):
	Codon = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP", "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R", "CGA": "R",
	    "CGG": "R", "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T", "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R", "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E", "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", "UAA":" ", "UAG":" ","UGA":" "}
	protein = ""
	i=0
	while i <(len(RNA)):
		protein += Codon[RNA[i:i+3]]
		i=i+3
	return protein
	
def transcribe(DNA):
	seq = 'ATCGAUCG'
	RNA_dict = {seq[i]:seq[i+4] for i in range(4)}
	return ''.join([RNA_dict[base] for base in DNA])

def ReverseComplement(DNA):
	Complement=""
	for i in range (len(DNA)):
		if DNA[len(DNA)-i-1]=="A":
			Complement += "T"
		if DNA[len(DNA)-i-1]=="T":
			Complement += "A"
		if DNA[len(DNA)-i-1]=="G":
			Complement += "C"
		if DNA[len(DNA)-i-1]=="C":
			Complement += "G"
	return Complement
	
def SubstringDNAofProtein(DNA, protein):
	RNA=transcribe(DNA)
	RNAR=transcribe(ReverseComplement(DNA))
	window=len(protein)*3
	encoding=[]
	i=0
	while i<(len(RNA)-window):
		if CodonTranslate(RNA[i:i+window])==protein:
			encoding.append(DNA[i:i+window])
		if CodonTranslate(RNAR[i:i+window])==protein:
			encoding.append(DNA[len(RNA)-i-window:len(RNA)-i])
		i=i+1
	return encoding
	
	
	
	
if __name__ == "__main__":
	#RNA="AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
	#RNA=open("dataset_96_4.txt").read()
	#DNA="ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
	#protein="MA"
	protein="YGMWMWWYN"
	DNA=open("dataset_96_7.txt").read()
	#print (CodonTranslate(RNA)) 
	print (*SubstringDNAofProtein(DNA,protein))
	
