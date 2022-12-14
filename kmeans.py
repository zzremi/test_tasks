'''
Two dimensional k-means algorithm for two clusters of data
'''


import numpy as np
import matplotlib.pyplot as plt
import time
	
	
def joindist(s0, s1):

	t = np.vstack((s0,s1))
	temp = np.random.permutation(np.arange(t.shape[0]))
	res = np.zeros(t.shape)
	for i in range(len(temp)):
		res[i,:] = t[temp[i],:]
	return res

	
def border_line(x0, y0, x1, y1, par=1, eps=1e-8):

	ang = (max((y1-y0),eps))/(max((x1-x0),eps))
	res_a = -1/ang	
	
	xm = (x0+par*x1)/(par+1);
	ym = (y0+par*y1)/(par+1);
	res_b = ym - xm*res_a
	
	return res_a, res_b
	

def partial_mean(arr, marks, target_val=1):

	count, val = 0, 0
	for i in range(len(arr)):
		if (marks[i] == target_val):
			count += 1
			val += arr[i]
	if (count > 0):
		return val/count
	else:
		return 0


def kmeans(dist, par=1, eps=1e-8, max_iter=500):

	mx0, my0, mx1, my1 = 0, 0, np.mean(dist[:,0]), np.mean(dist[:,1])
	s = dist.shape[0]
	t = np.zeros((s,1))
	for i in range(max_iter):
		a, b = border_line(mx0,my0,mx1,my1,par)
		for j in range(s):
			if (a*dist[j,0]+b > dist[j,1]):
				t[j] = 1
			else:
				t[j] = 0
		mx0_n = partial_mean(dist[:,0],t,0)
		my0_n = partial_mean(dist[:,1],t,0)
		mx1_n = partial_mean(dist[:,0],t,1)
		my1_n = partial_mean(dist[:,1],t,1)

		if (np.abs(mx0_n-mx0)+np.abs(my0_n-my0)+np.abs(mx1_n-mx1)+np.abs(my1_n-my1) < eps):
			return a, b, i
		else:
			mx0 = mx0_n
			mx1 = mx1_n
			my0 = my0_n
			my1 = my1_n
			plt.scatter(mx0,my0,color='orange',marker='x')
			plt.scatter(mx1,my1,color='red',marker='x')
	return a, b, i
			
	
if __name__ == "__main__":
	
#	distance_euclidean = lambda x,y: np.sqrt(x*x + y*y)
#	distance_max = lambda x,y: max(x,y)

	ti = time.time()
	cur_time = str(ti)
	pref = 'kmeans_try_'+cur_time[5:]+'_'
	
	n0, n1 = 15000, 1000

#	mx0, my0, mx1, my1 = 5, 15, 20, 30	
#	s0 = np.random.poisson(lam=(mx0, my0), size=(n0, 2))
#	s1 = np.random.poisson(lam=(mx1, my1), size=(n1, 2))

	mx0, my0, mx1, my1 = .1, .15, 4, 5
	lx0, ly0, lx1, ly1 = 1.5, 1.15, 2.20, 2.30
	sx0 = np.random.normal(mx0, lx0, size=(n0, 1))
	sy0 = np.random.normal(my0, ly0, size=(n0, 1))
	sx1 = np.random.normal(mx1, lx1, size=(n1, 1))	
	sy1 = np.random.normal(my1, ly1, size=(n1, 1))
	s0 = np.hstack((sx0,sy0))
	s1 = np.hstack((sx1,sy1))
	
	dist = joindist(s0,s1)
	
	for t in dist:
		t[0] = max(0,t[0])
		t[1] = max(0,t[1])
		
	plt.figure()
	plt.grid()
	
	plt.xlim(min(dist[:,0]),max(dist[:,0]))
	plt.ylim(min(dist[:,1]),max(dist[:,1]))
	
	plt.scatter(s0[:,0],s0[:,1],color='blue')
	plt.scatter(s1[:,0],s1[:,1],color='green')

#	dist = joindist(s0,s1)
#	plt.figure(figsize=(10,8))
#	plt.scatter(dist[:,0],dist[:,1])
	
	a, b, i = kmeans(dist)
	x = np.arange(0,35,0.1)
	y = a*x + b
	plt.scatter(x,y,color='red')
	plt.title('Border after %s iterations'%(str(i)))
	plt.savefig(pref + 'fin.png', dpi = 400)
	plt.cla()
	
	tval = round(time.time() - ti)
	print(i,'iterations processed in',str(tval),'sec')
	
	