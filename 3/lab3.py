f = open('names.txt', 'r')
n = {}
for line in f:
	b = line.split()
	average = (int(b[3])+int(b[4])+int(b[5]))/3
	b[3] += " " + b[4] + " " + b[5]
	del(b[5]); del(b[4])
	b[-1] +=  " -> " + str(average)
	j = b[0]+b[1]
	n[j] = b
	b[0] += " " + b[1]
	del(b[1])

for key in sorted(n.keys(),reverse=True):
	print (" | ".join(n[key]))






	
