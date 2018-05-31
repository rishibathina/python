
'''
A positive integer n is called double-perfect if the sum of its proper divisors equals 2n.There are only two 3-digit double-perfect number. What are they?
'''

#There are two ways.

#One is just createing a for loop
for n in range(100,1000):
    total_sum = 0       
    for e in range(1,n):
        if n % e == 0:
            total_sum += e
    if total_sum == 2 * n:
        print ("The only three digit perfect number is " + str(n))       

#The other one is by creating a function
def sum_of_proper_divs(n):
    '''sum_of_proper_divs(n) -> int
    returns the sum of the proper divisors of n'''
    total = 0 # intialize the sum
    for div in range(1,n):
        # check if div is a proper divisor
        if n % div == 0:  
            total += div  # add div to the sum
    return total

# check every 3-digit number
for num in range(100,1000):
    if 2*num == sum_of_proper_divs(num):
        # we found one!
        print(str(num) + " is double-perfect!")