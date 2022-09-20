import numpy as np

def PatternCount(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:(i+len(pattern))] == pattern:
            count += 1
    return count

def FrequentWords(text,k):
	FrequentPatterns=set ()
	kmercount=[None]*(len(text)-k+1)
	for i in range (len(text)-k+1):
		pattern= text[i:(i+k)]
		kmercount[i]=PatternCount(text, pattern)
	maxCount= np.max(kmercount)
	print (maxCount)
	for  i in range (len(text)-k+1):
		if kmercount[i] == maxCount:
			FrequentPatterns.add (text[i:(i+k)])
	return FrequentPatterns

	
if __name__ == "__main__":
	text= open('FrequentWord.txt', 'r').read()
	k = int(input("What is your k? "))
	print (FrequentWords(text, k))