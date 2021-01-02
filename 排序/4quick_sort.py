import random
from cal_time import *

def partition(lst,left,right):

	temp = lst[left]
	while left < right:
		# 右边查找
		while left < right and lst[right] >= temp:
			right -= 1
		lst[left] = lst[right]
		# 左边查找
		while left < right and lst[left] <= temp:
			left += 1
		lst[right] = lst[left]
	lst[left] = temp
	return left

# O(nlogn) 
def _quick_sort(lst,left,right):

	if left < right:
		mid = partition(lst,left,right)
		_quick_sort(lst,left,mid-1)
		_quick_sort(lst,mid+1,right)

@cal_time
def quick_sort(lst):
	_quick_sort(lst,0,len(lst)-1)
	



a = list(range(10000))
random.shuffle(a)
quick_sort(a) 
#print(a)