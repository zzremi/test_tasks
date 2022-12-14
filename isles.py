'''
Solving tis:
https://leetcode.com/problems/number-of-islands/
'''


import numpy as np

def fill_rand(n,m,p):

    s = np.zeros((n,m),np.int16)
    for i in range(0,n):
        for j in range(0,m):
            r = np.random.normal(0,1)
            if (r > p):
                s[i,j] = 1
	
    return s

	
def draw(s):

    n, m = s.shape
    for i in range(0,n):
        str = ""
        for j in range(0,m):    
            if (s[i,j] > 0):
                str = str + "+"    #"■"
            else:
                str = str + " "    #"□"
        print(str)
	

def fill(input, output, pos0, pos1, val):

    n, m = s.shape
    output[pos0,pos1] = val
    if (pos0 < m-1):
        if ((input[pos0+1,pos1] > 0) and (output[pos0+1,pos1] != val)):
            fill(input, output, pos0+1, pos1, val)
    if (pos0 > 0):
        if ((input[pos0-1,pos1] > 0) and (output[pos0-1,pos1] != val)):
            fill(input, output, pos0-1, pos1, val)
    if (pos1 < m-1):
        if ((input[pos0,pos1+1] > 0) and (output[pos0,pos1+1] != val)):
            fill(input, output, pos0, pos1+1, val)
    if (pos1 > 0):
        if ((input[pos0,pos1-1] > 0) and (output[pos0,pos1-1] != val)):
            fill(input, output, pos0, pos1-1, val)


if __name__ == "__main__":
    
    n, m = 20, 20
    p = 0.5

    s = fill_rand(n,m,p)
    print(s)
    print(n,m,sum(sum(s))/(n*m))
    draw(s)
    
    t = np.zeros((n,m),np.int16)
    count = 0
	
    for i in range(0,n):
        for j in range(0,m):
            if ((s[i,j] > 0) and (t[i,j] == 0)):
                count = count +1
                fill(s,t,i,j,count)
    
    print(count)
    print(t)
                	
	