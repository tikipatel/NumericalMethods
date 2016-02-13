import matplotlib.pyplot as plt

def collatz_sequence(x):
	seq = [x]
	if x < 1:
	   return []
	while x > 1:
	   if x % 2 == 0:
		 x = x / 2
	   else:
		 x = 3 * x + 1 
	   seq.append(x)    # Added line
	return seq

#lengths = []
#myRange = range(4,1000000)
#for i in myRange:
#	lengths.append(len(collatz_sequence(i)))
#plt.plot(lengths)
#plt.show()
mySeq = collatz_sequence(670617279)
print(mySeq)
plt.plot(mySeq)
plt.show()