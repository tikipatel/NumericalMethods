def sievePrimes(maximum):
    primes = dict.fromkeys(range(3,maximum+1,2),True)
    sieveList = [2]
    for num in sorted(primes):
        if primes[num] == True:
            sieveList.append(num)
            j = num ** 2
            while j < maximum:
                if j in primes:
                    primes[j] = False
                j += num
    return(sieveList)

largestPrime = 1000000
x = sievePrimes(largestPrime)
print("The number of primes under " + str(largestPrime) + " is " + str(len(x)) + ".")
#print(x)
largest = 0
index = 0
gapsList = []
for idx, val in enumerate(x):
    if idx < len(x)-1:
        gapsList.append((x[idx+1] -val))
        if (x[idx+1] -val) >= largest:
            largest = (x[idx+1] - val)
            index = idx
print("The largest gap between two primes under " + str(largestPrime) + " is " + str(largest) + ". The index of this number is " + str(index) + ". This gap happens between " + str(x[index]) + " and " + str(x[index+1]) + ".")
avegrage = 0
total = 0
for i in gapsList:
    total += i
avegrage = total/len(gapsList)
print("The average gap between two primes under " + str(largestPrime) + " is " + str(avegrage) + ".")

#import string
#
#def alphaColumn(number):
#    if number < 1:
#        return "There needs to be at least one column"
#    final = number
#    alphabet = (list(string.ascii_uppercase))
#    columnString = ""
#    while final > 0:
#        modulo = (final - 1) % 26
#        columnString = alphabet[modulo] + columnString 
#        final = ((final - modulo) / 26)
#    return columnString
#
#def excel2num(x): 
#    return reduce(lambda s,a:s*26+ord(a)-ord('A')+1, x, 0)
#    
#x = 3703
#while x > 0:
#    m = 3703 - x
#    print([m, alphaColumn(m), excel2num(alphaColumn(m))])
#    x = x - 1
