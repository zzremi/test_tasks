'''
Two dimensional EM algorithm for two clusters of data
'''

import numpy as np
import scipy.stats as sc
import matplotlib.pyplot as plt
import time


def generate_two_2d_nd(n0, n1, mx0, my0, mx1, my1, lx0, ly0, lx1, ly1):
	
	sx0 = np.random.normal(mx0, lx0, size=(n0, 1))
	sy0 = np.random.normal(my0, ly0, size=(n0, 1))
	sx1 = np.random.normal(mx1, lx1, size=(n1, 1))	
	sy1 = np.random.normal(my1, ly1, size=(n1, 1))
	s0 = np.hstack((sx0,sy0))
	s1 = np.hstack((sx1,sy1))
	return s0, s1
	
	
def joindist(s0, s1):

	t = np.vstack((s0,s1))
	a = np.hstack((np.zeros(s0.shape[0]),np.ones(s1.shape[0])))
	temp = np.random.permutation(np.arange(t.shape[0]))
	res = np.zeros(t.shape)
	ans = np.zeros((t.shape[0],1))
	for i in range(len(temp)):
		res[i,:] = t[temp[i],:]
		ans[i] = a[temp[i]]
	return res, ans

	
def form_dist(dist,ans):
	
	l0 = len(ans) - int(np.sum(ans))
	l1 = int(np.sum(ans))
	s0 = np.zeros((l0,2))
	s1 = np.zeros((l1,2))
	j0 = 0
	j1 = 0
	
	for i in range(len(ans)):
		if (ans[i] > 0):
			s1[j1,0] = dist[i,0]
			s1[j1,1] = dist[i,1]
			j1 +=1
		else:		
			s0[j0,0] = dist[i,0]
			s0[j0,1] = dist[i,1]
			j0 +=1
			
	return s0, s1
	
	
def draw_dist(dist,ans,act,pref,i):

	s0, s1 = form_dist(dist, ans)

	if (i > 0):
	
		plt.figure()
		plt.grid()
		plt.xlim(min(dist[:,0]),max(dist[:,0]))
		plt.ylim(min(dist[:,1]),max(dist[:,1]))

		plt.scatter(s0[:,0],s0[:,1],color='blue',s=5)
		plt.scatter(s1[:,0],s1[:,1],color='green',s=5)
		
		eval = 100 * np.sum(np.abs(ans - act)) / len(act)
		plt.title('After %s iterations of EM, error: %.3f%%'%(str(i),eval))

		plt.savefig(pref + 'iter=' + str(i) + '.png', dpi = 400)
		plt.cla()
	
	return s0, s1

	
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
			plt.scatter(mx0,my0,color='yellow',marker='x')
			plt.scatter(mx1,my1,color='orange',marker='x')
	return a, b, i
	

def em(dist, ans, act, pref='', eps=100, max_iter=50):

	s = dist.shape[0]
	
	for i in range(max_iter):
	
		s0, s1 = draw_dist(dist,ans,act,pref,i)
		ndx0 = sc.norm(np.mean(s0[:,0]),np.std(s0[:,0]))
		ndy0 = sc.norm(np.mean(s0[:,1]),np.std(s0[:,1]))
		ndx1 = sc.norm(np.mean(s1[:,0]),np.std(s1[:,0]))
		ndy1 = sc.norm(np.mean(s1[:,1]),np.std(s1[:,1]))
		rat = np.sum(ans) / (len(ans) - np.sum(ans))
		ans_n = np.zeros((s,1))
		
		for j in range(s):
			p0 = ndx0.pdf(dist[j,0])*ndy0.pdf(dist[j,1])
			p1 = ndx1.pdf(dist[j,0])*ndy1.pdf(dist[j,1])
			if (p1*rat > p0):
				ans_n[j] = 1
			else: 
				ans_n[j] = 0
		
		nval = np.sum(np.abs(ans_n - ans))
		eval = np.sum(np.abs(ans_n - act)) / len(act)
		print('iteration :',i,'| updated:',round(nval),'| eval: ','{:.3f}'.format(100*eval),'%')
		
		if (nval > eps):
			ans = ans_n
		else:
			return ans_n, i	
			
	return ans_n, i

	
if __name__ == "__main__":
	
#	distance_euclidean = lambda x,y: np.sqrt(x*x + y*y)
#	distance_max = lambda x,y: max(x,y)

	ti = time.time()
	cur_time = str(ti)
	pref = 'em_try_'+cur_time[5:]+'_'
	
	n0, n1 = 10000, 5000
#	n0, n1 = 15000, 1000

#	mx0, my0, mx1, my1 = 5, 15, 20, 30	
#	s0 = np.random.poisson(lam=(mx0, my0), size=(n0, 2))
#	s1 = np.random.poisson(lam=(mx1, my1), size=(n1, 2))

	mx0, my0, mx1, my1 = .1, .15, 1.2, 1.8
	dx0, dy0, dx1, dy1 = 1.50, 1.25, 3.20, 4.40
	
#	mx0, my0, mx1, my1 = .1, .15, 4, 5
#	dx0, dy0, dx1, dy1 = 1.5, 1.15, 2.20, 2.30
	
	s0, s1 = generate_two_2d_nd(n0, n1, mx0, my0, mx1, my1, dx0, dy0, dx1, dy1)	
	dist, act = joindist(s0,s1)
	
	for t in dist:
		t[0] = max(0,t[0])
		t[1] = max(0,t[1])
		
	plt.figure()
	plt.grid()
	plt.xlim(min(dist[:,0]),max(dist[:,0]))
	plt.ylim(min(dist[:,1]),max(dist[:,1]))	
		
	a, b, i = kmeans(dist)
	
	x = np.arange(0,50,0.01)
	y = a*x + b
	
	tval = round(time.time() - ti)
	print(i,'iterations processed in',str(tval),'sec')
	
	plt.scatter(s0[:,0],s0[:,1],color='blue',s=5)
	plt.scatter(s1[:,0],s1[:,1],color='green',s=5)
	plt.scatter(x,y,color='red',s=4)

	ans = np.zeros((dist.shape[0],1))
	for j in range(len(ans)):
		if ((a*dist[j,0]+b) < dist[j,1]):
			ans[j] = 1			

#	s0, s1 = form_dist(dist, ans)
#	plt.scatter(s0[:,0],s0[:,1],color='blue',s=5)
#	plt.scatter(s1[:,0],s1[:,1],color='green',s=5)		

	eval = np.sum(np.abs(ans - act)) / len(act)
	plt.title('After %s iterations, error: %.3f%%'%(str(i),100*eval))
	plt.savefig(pref + 'init.png', dpi = 400)
	plt.cla()
	
	print('init eval:','{:.3f}'.format(100*eval),'%')
	ans_n, i = em(dist,ans,act,pref)
	
	tval = round(time.time() - ti)
	print('time elapsed after', str(i), 'iterations of em:',str(tval),'sec')
	
#	plt.figure()
#	plt.grid()
#	plt.xlim(min(dist[:,0]),max(dist[:,0]))
#	plt.ylim(min(dist[:,1]),max(dist[:,1]))	
#	plt.scatter(s0[:,0],s0[:,1],color='blue',s=5)
#	plt.scatter(s1[:,0],s1[:,1],color='green',s=5)
#	plt.title('Original distributions')
#	plt.savefig(pref + 'orig.png', dpi = 400)
#	plt.cla()	
	
