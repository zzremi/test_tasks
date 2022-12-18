'''
Generate and draw binary tree, also solving this:
https://leetcode.com/problems/path-sum-ii/
'''


import numpy as np


class BinTreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

		
def generate_rand(nmax, left_weigth = 0, right_weigth = 0):

    if (nmax > 0):
        r = np.random.normal(0,1)
        t = BinTreeNode(round(r*10))
        r = np.random.normal(0,1)
        if (r > left_weigth):
            t.left = generate_rand(nmax-1)
        r = np.random.normal(0,1)
        if (r > right_weigth):
            t.right = generate_rand(nmax-1)			
        return t
    else:
        return None
	

def draw(t, layer = 0, pref = ""):

    print(layer,":",pref,"| value = ",t.value)
    if (t.left != None):
        draw(t.left,layer+1,pref+"l")
    if (t.right != None):
        draw(t.right,layer+1,pref+"r")
		
	
def form_str(t, s, nl, pos, num, layer = 0):

    if (layer == num):
        return s[0:pos] + str(t.value) + s[pos+1:]
    else:
        if (t.left != None):
            s = form_str(t.left,s,nl,pos-2**(nl-layer-1),num,layer+1)
        if (t.right != None):
            s = form_str(t.right,s,nl,pos+2**(nl-layer-1),num,layer+1)
        return s

		
def get_number_of_layers(t, num = 0):

    if ((t.left == None) and (t.right == None)):
        return num
    if (t.left != None):
        num_left = get_number_of_layers(t.left, num+1)		
    else:
        num_left = 0
    if (t.right != None):
        num_right = get_number_of_layers(t.right, num+1)		
    else:
        num_right = 0	
    return max(num_left,num_right)
	
	
def form_sum_dict(t, d, pref='h', sum=0):

	sum += t.value
	if ((t.left == None) and (t.right == None)):
		d[pref] = sum
	else:
		if (t.left != None):
			form_sum_dict(t.left, d, pref+'l', sum)
		if (t.right != None):
			form_sum_dict(t.right, d, pref+'r', sum)	
			
	
if __name__ == "__main__":
    
	n = 8
	target_sum  = 0
	
	t = generate_rand(n)
	draw(t)
	nl = get_number_of_layers(t)
	print('\n')
	for i in range(0,nl+1):
		s = ""
		for j in range(0,2**(nl+1)):
			s = s + "_"
		print(i,":",form_str(t, s, nl, 2**nl, i))
		
	d = {}
	form_sum_dict(t,d)
	print('\n')
	[print(k,'|',d[k]) for k in d]
	print('\n')
	klist = list(d.keys())
	vlist = list(d.values())	
	if (target_sum in vlist):
		print(klist[vlist.index(target_sum)])
	else:
		print('None')
	
	
