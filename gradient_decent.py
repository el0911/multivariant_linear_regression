import numpy as np

real=[]
with open('fish.txt') as f:
    result = [line.rstrip('\n').split(',') for line in f]

result=np.array(result,dtype=float)
real=np.array(result,dtype=float )

j=np.zeros(len(result[0]))
j=np.array(j)
print(j)
for x in range(10000):

	pass
