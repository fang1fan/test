# 顺序查找，时间复杂度O（n)

def linear_search(l, val):
	for ind, v in enumerate(l):
		if v == val:
			return ind
	else:
		return None

print(linear_search([2,6,8,4], 5))
