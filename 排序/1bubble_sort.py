'''
冒泡排序：时间复杂度O（n2)
第一个循环遍历n-1趟
每趟需要比较n-i-1次

冒泡排序改进版：
如果有一趟循环没有交换位置，说明未排序区已经有序。

'''
import random
from cal_time import *

@cal_time
def bubble_sort(l):
	n = len(l)
	exchange = False
	for i in range(n-1):
		for j in range(n-i-1):
			if l[j] > l[j+1]:
				l[j],l[j+1] = l[j+1],l[j]
				exchange = True

		if not exchange:
                        return l

	return l

li = list(range(10000))
random.shuffle(li)
bubble_sort(li)
