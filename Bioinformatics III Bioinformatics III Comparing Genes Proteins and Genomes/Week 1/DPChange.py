import math
# The minimum number of coins with denominations Coins that changes money
def DPChange(money, Coins):
	MinNumCoins={i:math.inf for i in range (money+1)}
	MinNumCoins[0]=0
	for m in range (1,money+1):
			for i in range (len(Coins)):
				if m>=Coins[i]:
					# replace with the minium number and store in dict
					if MinNumCoins[m-Coins[i]]+1<MinNumCoins[m]:
						MinNumCoins[m]=MinNumCoins[m-Coins[i]]+1
	return MinNumCoins[money]

if __name__ == "__main__":
	Coins=[24,5,3,1]
	money=16032
	print (DPChange(money, Coins))