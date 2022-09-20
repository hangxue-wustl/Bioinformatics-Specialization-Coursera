# A collection of space-separated integers specifying all starting positions where Pattern appears as a substring of Genome
# Sample Input:
# ATAT
# GATATATGCATATACTT
# Sample Output:1 3 9


def PatternMatch(text, pattern):
    Position = []
    for i in range(len(text) - len(pattern)+1):
    	if text[i:i + len(pattern)] == pattern:
        	Position.append(i)
    print(*Position)


if __name__ == "__main__":
    text = open('PatternMatch.txt', 'r').read()
    pattern = input("What is your pattern? ")
    print(PatternMatch(text, pattern))
