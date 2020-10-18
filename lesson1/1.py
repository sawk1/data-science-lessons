import numpy as np 

#Задание 1

a=np.array([[1,6],
	[2,8],
	[3,11],
	[3,10],
	[1,7]])

mean_a=np.mean(a, axis=0)

print(mean_a)

#Задание 2
print(a[:,0])
a_centered=np.vstack(((a[:,0]-mean_a[0]),(a[:,1]-mean_a[1]))).T
print(a_centered,a_centered.shape )

#Задание 3

a_centered_sp=a_centered[:,0]@a_centered[:,1]/(a.shape[0]-1)

print(a_centered_sp)

#Задание 4

covar=np.cov(a.T)[0,1]
print(covar)