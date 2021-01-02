import random
from cal_time import *

def merge(lst, low, mid, high):
	i = low
	j = mid + 1
	lst1 = []
	while i <= mid and j <= high:
		if lst[i] <= lst[j]:
			lst1.append(lst[i])
			i += 1
		else:
			lst1.append(lst[j])
			j += 1
	while i <= mid:
		lst1.append(lst[i])
		i += 1
	while j <= high:
		lst1.append(lst[j])
		j += 1
	lst[low:high+1] = lst1


def _merge_sort(lst, low, high):
	if low < high:
		mid = (low + high) // 2
		_merge_sort(lst, low, mid)
		_merge_sort(lst, mid + 1, high)
		merge(lst, low, mid, high)

@cal_time
def merge_sort(lst):
	return _merge_sort(lst, 0, len(lst) - 1)


a = list(range(10000))
random.shuffle(a)
merge_sort(a)
#print(a)
