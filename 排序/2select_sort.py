'''
选择排序：
'''
import random
from cal_time import *

@cal_time
def select_sort(l):
	n = len(l)
	for i in range(n-1):
		min_ind = i
		for j in range(i,n):
			if l[j] < l[min_ind]:
				min_ind = j
		l[i],l[min_ind] = l[min_ind],l[i]
	return l

li = list(range(10000))
random.shuffle(li)
select_sort(li)