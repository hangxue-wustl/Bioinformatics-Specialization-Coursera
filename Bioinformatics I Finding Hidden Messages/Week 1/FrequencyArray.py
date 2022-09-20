# dictionary in Python
# thisdict = {"brand":"Ford","model":"Mustang","year":1964}


def PatternToNumber(Pattern):
    n = 0
    seq1 = 'ACGTacgt01230123'
# 	A:0, C:1, G:2, T:3
    seq_dict = {seq1[i]: int(seq1[i+8]) for i in range(8)}
    l = len(Pattern.strip())
    for i in range(l):
        n += seq_dict[Pattern[i]]*4**(l-i-1)
    return n


def NumberToPattern(n, k):
    p = []
    seq1 = '0123ACGT'
    seq_dict = {int(seq1[i]): seq1[i+4] for i in range(4)}
    for i in range(k):
        p.insert(0, seq_dict[n % 4])
        n //= 4
    return ''.join(p)


def ComputingFrequencies(Text, k):
    frequencyArray = [0]*(4**k-1)
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        j = PatternToNumber(Pattern)
        frequencyArray[j] = frequencyArray[j] + 1
    return frequencyArray

# Total runtime is O(|Genome| * (L * k + 4^k)). Still terrible
# ClumpFinding not tested
# It would be a lot faster to go through and count the patterns for the whole genome, and 
# store the locations of patterns as well as the number of times that they occurred. Then 
# you could loop through the frequency array once, and if the index was greater than t, you 
# would check if t of the locations were within L of each other.  That would mean storing a 
# dataset that is the same size as the genome (for the location of each pattern) but it 
# would run way faster: O(|Genome|+4^k).

def ClumpFinding (Genome, k, L, t)
	FrequentPatterns= set()
	Clump = [0]*(4**k-1)
	for i in range(len(Genome)-L+1):
		Text=Genome[i:i+L]
		FrequencyArray =ComputingFrequencies(Text, k)
		for i in range (4*k−1):
            if FrequencyArray[i] >= t:
                Clump[i]=1
	for i in range (4*k−1):
		Pattern=NumberToPattern(i, k)
        FrequentPatterns.add (Pattern)
    return FrequentPatterns

if __name__ == "__main__":
    Text = open('FrequencyArray.txt', 'r').read()
    k = int(input("What is your k? "))
    print(*ComputingFrequencies(Text, k))
