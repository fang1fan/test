'''
插入排序：
'''
import random
from cal_time import *

@cal_time
def insert_sort(l):
	n = len(l)
	for i in range(1,n):
		i_val = l[i]
		j = i-1
		while j>=0 and i_val < l[j]:
			l[j+1] = l[j]
			j = j-1
		else:
			l[j+1] = i_val	
	return l

li = list(range(10000))
random.shuffle(li)
insert_sort(li)


