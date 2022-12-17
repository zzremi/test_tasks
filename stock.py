'''
Solviing this:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
'''


import numpy as np


def generate_array(n, m, s):
    return np.array([max(0,round(np.random.normal(m,s))) \
	for _ in range(n)])
	
	
def generate_list_indiscriminate(outer_list, inner_list, length, pos = 0):
	
	outer_list.append(inner_list)
	if (pos < length - 1):
		generate_list_indiscriminate(outer_list, inner_list, length, pos+1)
		generate_list_indiscriminate(outer_list, inner_list  + [pos], length, pos+1)
	else:
		outer_list.append(inner_list + [pos])

		
def generate_list(outer_list, inner_list, arr, fee = 0, cooldown = 0, pos = 0):
	
	if ((len(inner_list) > 1) and (len(inner_list)%2 == 0)):
		outer_list.append(inner_list)
	if (pos < len(arr) - 1):
		generate_list(outer_list, inner_list, arr, fee, cooldown, pos+1)
		if (len(inner_list)%2 == 1):
			if(arr[pos]-arr[inner_list[-1]] > fee):
				generate_list(outer_list, inner_list  + [pos], arr, fee, cooldown, pos+1)
		else:
			if ((len(inner_list) < 1) or (pos-inner_list[-1]>cooldown)):
					generate_list(outer_list, inner_list  + [pos], arr, fee, cooldown, pos+1)	
	else:
		if (len(inner_list)%2 == 1):
			outer_list.append(inner_list + [pos])

		
def profit_sum(arr, x, cooldown = 0, fee = 0):

	if ((len(x) < 2) or (len(x)%2 != 0)):
		return -1
		
	pos_0 = x[0]
	pos_1 = x[1]
	t = (arr[pos_1] - arr[pos_0] - fee)

	if (len(x) > 2):
		for i in range(1,len(x)//2):
			npos_0 = x[2*i]
			npos_1 = x[2*i+1]
			if (not x[2*i] > pos_1 + cooldown):
				return -1
			else:
				pos_0 = x[2*i]
				pos_1 = x[2*i+1]
				t += (arr[pos_1] - arr[pos_0] - fee)
		return t
	else:
		return t
		

if __name__ == "__main__":
	
	arr = generate_array(16,6,8) + 1
	
	print(len(arr),np.arange(len(arr)))
	print(len(arr),arr)
	print('\n')	

	cooldown = 1
	fee = 2
	
	outer_list = []
	inner_list = []
	generate_list_indiscriminate(outer_list, inner_list, len(arr))	
	print('indiscriminate list size',len(outer_list))
	
	res = []
	[res.append(profit_sum(arr, order, cooldown, fee)) for num, order in enumerate(outer_list)]
	
	m = max(res)
	print('result :',max(res))	
	[print(num,order) for num, order in enumerate(outer_list) \
	if profit_sum(arr, order, cooldown, fee) == m]
	print('\n')	
	
	
	outer_list = []
	inner_list = []
	generate_list(outer_list, inner_list, arr, fee, cooldown)	
	print('list size',len(outer_list))
	
	res = []
	[res.append(profit_sum(arr, order, cooldown, fee)) for num, order in enumerate(outer_list)]
	
	m = max(res)
	print('result :',max(res))	
	[print(num,order) for num, order in enumerate(outer_list) \
	if profit_sum(arr, order, cooldown, fee) == m]
	
	