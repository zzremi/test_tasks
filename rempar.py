'''
Solviing this:
https://leetcode.com/problems/remove-invalid-parentheses/
'''


import numpy as np


def generate_rand(n, so="(", sc=")"):

    s = ""
    for i in range(0,n):
        r = np.random.normal(0,1)
        if (r > 0):
            s = s + sc
        else:
            s = s + so
			
    return s
	

def check(s, so="(", sc=")"):

    c0, c1 = 0, 0
    for i in range(0,len(s)):
        if (s[i] == sc):
            c1 = c1 +1
            if (c1 > c0):
                return False
        else:
            if (s[i] == so):
                c0 = c0 + 1

    return c0 == c1

	
def form(s, s_list, n_list, pos, val, so="(", sc=")"):

    if check(s):
        print(val,s)
        n_list.append(val)
        s_list.append(s)
    else:
        for i in range(pos,len(s)):
            form(s[0:i]+s[i+1:],s_list,n_list,i,val+1)
	
	
if __name__ == "__main__":
    
    n = 10
    s = generate_rand(n)
    print("Original: ",s)	
    s_list, n_list = [], []

    if check(s):
        print("min = 0")
        print(s)
    else:
        form(s,s_list,n_list,0,0)
        m = min(n_list)
        print("min = ",m)
        [print(s_list[i]) for i in range(0,len(s_list)) if n_list[i]==m]
		
		
		
		
		
		
		