'''
Solving this:
https://leetcode.com/problems/merge-intervals/
'''


import numpy as np

		
def is_overlap(int_0, int_1):
	
	if ((int_0[1] < int_1[0]) or (int_1[1] < int_0[0])):
		return False
	else:
		return True
		
	
	if ((int_0[1] < int_1[0]) or (int_1[1] < int_0[0])):
		return False
	else:
		return True

		
if __name__ == "__main__":
    
	
	intervals = [[0,4], [2,6], [5,8], [10,13], [12,16]]
	
	new_intervals = intervals
	out_intervals = []
	
	while (len(new_intervals) > 0):
		nnew_intervals = []
		if (len(new_intervals) == 1):
			out_intervals.append(new_intervals[0])
		else:
			cur_min = new_intervals[0][0]
			cur_max = new_intervals[0][1]
			is_sep = True
			for i in range(1,len(new_intervals)):
				if is_overlap(new_intervals[0],new_intervals[i]):
					cur_min = min(cur_min,new_intervals[i][0])
					cur_max = max(cur_max,new_intervals[i][1])
					is_sep = False
				else:
					nnew_intervals.append(new_intervals[i])
			if (is_sep):
				out_intervals.append([cur_min,cur_max])
			else:
				nnew_intervals.append([cur_min,cur_max])
		print(new_intervals)
		print(nnew_intervals)
		print(out_intervals)
		print('\n')
		new_intervals = nnew_intervals
	
	print('input :',intervals)
	print('output :',out_intervals)
			
					
					
					
					
					
					
					