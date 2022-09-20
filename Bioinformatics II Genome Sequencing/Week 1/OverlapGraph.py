#almost correct, might have errors around '->', no duplicates in key
import sys


def OverlapGraph(kmer):
    adjacent_list = {kmer[i]: set() for i in range(len(kmer))}
    for m in adjacent_list:
        for n in kmer:
            if m[1:] == n[:-1]:
                adjacent_list[m].add(n)
    return adjacent_list


if __name__ == "__main__":
    data = list(sys.stdin.read().strip().split())
    adjacent_list = OverlapGraph(data)
    for m, n in adjacent_list.items():
    	if len(n)>0:
    		print(m+' -> '+','.join(n))
