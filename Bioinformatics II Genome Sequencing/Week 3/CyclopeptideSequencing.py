def CyclopeptideSequencing(Spectrum,aminoAcidMassdict):
	CandidatePeptides=()
	FinalPeptides=[]
	for i in range (len(Spectrum)):
		for s in aminoAcidMassdict:
			if s==Spectrum[i]:
				CandidatePeptides.add(Spectrum[i])
	while len(CandidatePeptides)>0:
		CandidatePeptides=expand(CandidatePeptides)
		deletions=[]
		for p in CandidatePeptides:
			if Mass(CandidatePeptides)>=Spectrum[-1:]:
				if CircularSpectrum(CandidatePeptides,aminoAcidMassdict)=Spectrum:
					FinalPeptides.append(p)
				deletions.append(p)
			else if Isconsistent(p,Spectrum)!=True:
				deletions.append(p)
		for d in deletions:
			peptides.remove(p)
	return FinalPeptides
				
def expand(peptide,aminoAcidMassdict):
	#add one mass at the end of each peptide
	for p in peptide:
		for s in aminoAcidMassdict:
			peptide.add(p+'-'+aminoAcidMassdict[s])
	return peptide

def Isconsistent(p,Spectrum):
	individual = [int(individual) for individual in p.split('-')]
	#unfinished
	Linear=LinearSpectrum(individual,aminoAcidMassdict)
	 
		


def LinearSpectrum(peptide,aminoAcidMassdict):
	l=len(peptide)
	PrefixMass=[0]*l*(l)
	PrefixMass[0]=0
	for i in range (1,l+1):
		for s in aminoAcidMassdict:
			if s==peptide[i-1]:
				PrefixMass[i]=PrefixMass[i-1]+aminoAcidMassdict[s]
	LinearSpectrum=[]
	m=len(PrefixMass)
	for i in range (l):
		for j in range (i+1,l+1):
			LinearSpectrum.append(PrefixMass[j]-PrefixMass[i])
	LinearSpectrum.append(0)
	return LinearSpectrum
	
def CircularSpectrum(peptide,aminoAcidMassdict):
	prefix=peptide[:-1]
	Linear=LinearSpectrum(prefix,aminoAcidMassdict)
	totalmass=0
	for i in range (len(peptide)):
		for s in aminoAcidMassdict:
			if s==peptide[i]:
				totalmass=aminoAcidMassdict[s]+totalmass
	difference=[]
	for i in Linear:
		difference.append (totalmass-i)
	answer=difference+Linear
	answer.sort()
	return answer
	
	
def subpeptides(peptide):
	looped=peptide+peptide
	sub=[]
	for start in range(0, len(peptide)):
		for length in range (1, len(peptide)):
			sub.append(looped[start:start+length])
	sub.append(peptide)
	return sub
			
	
if __name__ == "__main__":
	aminoAcid = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'L', 'N', 'D', 'K', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
	aminoAcidMass = [ 57, 71, 87, 97, 99, 101, 103, 113, 113, 114, 115, 128, 128, 129, 131, 137, 147, 156, 163, 186]
	aminoAcidMassdict={aminoAcid[i]:aminoAcidMass[i] for i in range (len(aminoAcid))}

	#RNA="AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
	#RNA=open("dataset_96_4.txt").read()
	#DNA="ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
	#protein="MA"
	peptide="LAEFPTVCQFESW"
	#print (LinearSpectrum(peptide)) 
	answer=CircularSpectrum(peptide,aminoAcidMassdict)
	#print (answer)
	for i in answer:
		print (i)
	
	
