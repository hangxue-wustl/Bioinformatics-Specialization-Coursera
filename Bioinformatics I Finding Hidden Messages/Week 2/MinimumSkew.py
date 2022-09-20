# min_position=[]; Initiate an empty list
# list1 = [0] * size; Initiate an array of 0s of size

def MinimumSkew(Genome):
    skew=0
    min_skew=0
    min_position=[]
    for i in range (len(Genome)):
        if Genome[i]=='C':
            skew-=1
            if skew == min_skew:
                min_position.append(i+1)
            if skew < min_skew:
                min_skew = skew
                min_position = [i+1]
        if Genome[i]=='G':
            skew += 1
    return min_position

if __name__ == "__main__":
	d=open("Salmonella_enterica.txt").readlines()
	d=d[1:-1]
	s=""
	for i in range (0,len(d)):
		s=s+d[i].strip('\n')
	print (MinimumSkew(s))	