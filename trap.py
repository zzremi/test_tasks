'''
Solviing this:
https://leetcode.com/problems/trapping-rain-water/
'''


import numpy as np


def generate_array(n,m,s):
    return np.array([max(0,round(np.random.normal(m,s))) for _ in range(n)])
	

def dsdiff(arr):
    
    res = np.diff(np.sign(np.diff(arr)))
    if (arr[0] > arr[1]):
        res = np.hstack(([-2],res))
    else:
        res = np.hstack(([0],res))
    if (arr[-1] > arr[-2]):
        res = np.hstack((res,[-2]))
    else:
        res = np.hstack((res,[0]))
    return res
	
	
def find_lmax(arr):
    
    temp = dsdiff(arr)
    res = []
    for i in range(len(arr)):
        if (temp[i] == -2):
            res.append(i)
    return np.array(res)
	
	
def mpos(arr):
    
    m = max(arr)
    return np.array([i for i in range(len(arr)) if arr[i] == m])[0]
	
	
if __name__ == "__main__":
	
	a = generate_array(15,4,6)

	arr = a.reshape(len(a),-1)
	d = np.diff(np.sign(np.diff(a))).reshape(len(a)-2,-1)
	r = dsdiff(a)
	lm = find_lmax(a)

#	print(np.hstack((arr,np.vstack(([[0]],np.vstack((d,[[0]])))))))
#	print(np.hstack((a.reshape(len(a),-1),r.reshape(len(a),-1))))
#	print(lm)

	fill = []
	mpos_l = 0
	mpos_r = mpos(a)
	
	for i in range(len(a)):
		if (not a[i] < a[mpos_l]):
			mpos_l = mpos(a[0:i+1])
		if (not a[i] > a[mpos_r]):
			mpos_r = mpos(a[i:])+i		
		fill.append(max(0,min(a[mpos_l],a[mpos_r])-a[i]))
#		fill.append(max(0,min(a[mpos(a[0:i+1])],a[mpos(a[i:])+i])-a[i]))
    
	for i in range(len(a)):
		str = ''
		for j in range(a[i]):
			str = str + '■'
		for j in range(fill[i]):
			str = str + 'X'	#□'
		print(str)    

	print('\n')
	print(sum(fill))
	
	
	
	