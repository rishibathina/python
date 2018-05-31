'''
There are two 3-digit numbers n having the property that $n$ is divisible by 11 and n/11 is equal to the sum of the squares of the digits of n.
'''
#First Loop through all three digit multiples of 11 staring with 110
for number in range (110, 1000, 11):
	#Check digits of n
	hundreds = number // 100
	tens = (number // 10) % 10
	ones = number % 10
	#Now check the case that we are looking for
	if number // 11 == hundreds ** 2 + tens ** 2 + ones ** 2:
		print (number)