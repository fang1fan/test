from cal_time import *
import random


# 一次向下调整，前提:节点的左右子树都是堆，但自身不是堆
def sift(lst,low,high):
	'''
	low:堆的根节点位置
	high:堆的最后一个节点位置
	'''
	temp = lst[low]
	i = low
	j = 2 * i + 1

	while j <= high:
		if j+1 <= high and lst[j+1] > lst[j]: # 若右孩子存在且大于左孩子
			j = j + 1
		if lst[j] > temp:
			# 更新i,j
			lst[i] = lst[j]
			i = j
			j = 2 * i + 1
		else:
			lst[i] = temp 
			break
	else:
		lst[i] = temp


@cal_time
# O(nlogn)
def heap_sort(lst):
	n = len(lst)
	# 构造堆
	for i in range((n-2)//2,-1,-1):
		# i表示构造堆时调整的堆的根位置
		sift(lst,i,n-1)

	# 
	for i in range(n-1,-1,-1):
		lst[0], lst[i] = lst[i], lst[0]
		sift(lst,0,i-1) # i-1是无序区最后一个元素


a = list(range(100000))
random.shuffle(a)
heap_sort(a)
#print(a)