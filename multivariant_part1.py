import numpy as np
# Iris-setosa = 1
# Iris-versicolor = 2
# Iris-virginica = 3
#for iris txt

def fname(x,real):
	x =(x * real.std())+real.mean()
	return x

def sweer():
	dss=[]
	s=0

	for res in range(len(result)):
		varr=result[s]
		#print(varr)
		#print(np.dot(varr,d))
		#varr=np.reshape(varr,(5,1))
		c=np.dot(varr,d)
		varr=np.subtract(y[s],c)
		#print('-')
		print(c)
		#print(y[s])
		print(varr)
		#print('-')
		dss.append(c)
		s=s+1

	dss=np.array(dss)
	ff=fname(dss,real)
	g=0
	for value in dss:
		print(real[g][len(result[0])-1])
		print(ff[g])
		g=g+1
	#dss=(dss - dss.mean())/dss.std()


real=[]
with open('fish.txt') as f:
    result = [line.rstrip('\n').split(',') for line in f]

result=np.array(result,dtype=float )
real=np.array(result,dtype=float )

#result=(result-result.mean())/result.std()
result=(result - result.mean())/result.std()
print(result.std())
y=[]
for r in result:
    y.append(r[len(result[0])-1])


y=np.array(y,dtype=float)
y=np.reshape(y,(1,len(result)))
print(np.shape(y))
#x
y=y.transpose()
result=np.delete(result,len(result[0]) - 1,1)
result=np.insert(result,0,1,axis=1)
transposed=np.dot(result.transpose(),result)
transposed=np.linalg.inv(transposed)
xty=np.dot(result.transpose(),y)
#sweer()
d=np.dot(transposed,xty)

print(d)

sweer()
#print(transposed[3:][1];)
