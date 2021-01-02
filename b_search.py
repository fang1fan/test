# 二分查找，时间复杂度O（logn)

def b_search(l, val):
    start = 0
    end = len(l) - 1
    while(start <= end):
        mid = (start + end) // 2
        if val < l[mid]:
            end = mid - 1
        elif val > l[mid]:
            start = mid + 1
        else:
            return mid
    else:
        return None


print(b_search([1,3,6,8,9,10],3))
            
