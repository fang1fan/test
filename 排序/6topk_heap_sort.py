from cal_time import *
import random

# topk问题：从长度为n的列表找出前K大的数

# 小根堆
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
		if j+1 <= high and lst[j+1] < lst[j]: # 若右孩子存在且小于左孩子
			j = j + 1
		if lst[j] < temp:
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
def topk(lst,k):
	heap = lst[:k]
	# 构造堆
	for i in range((k-2)//2,-1,-1):
		# i表示构造堆时调整的堆的根位置
		sift(heap,i,k-1)

	# 遍历
	for i in range(k,len(lst)):
		if lst[i] > heap[0]:
			heap[0] = lst[i]
			sift(heap,0,k-1)

	# 出数
	for i in range(k-1,-1,-1):
		heap[0], heap[i] = heap[i], heap[0]
		sift(heap,0,i-1) # i-1是无序区最后一个元素
	return heap

a = list(range(100000))
random.shuffle(a)
print(topk(a,10))
#print(a)