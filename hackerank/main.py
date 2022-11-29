import random

import postfix
import sort
from helper import check_order

def partition2(start, end, nums):
    ran = random.randint(start, end)
    pivot = end
    nums[pivot], nums[ran] = nums[ran], nums[pivot]

    border = start
    for cur in range(start, end):
        if nums[cur] >= nums[pivot]:
            nums[cur], nums[border] = nums[border], nums[cur]
            border += 1

    nums[border], nums[pivot] = nums[pivot], nums[border]
    return border

def partition(a, left, right):
    if left >= right:
        return
    ran = random.randint(left, right)
    a[ran], a[right] = a[right], a[ran]
    pivot = right
    p = left
    return p

def quick_select2(start, end, nums, k_largest):
    res = None
    while start <= end:
        p = partition(start, end, nums)
        if p == k_largest:
            res = nums[k_largest]
            break
        elif p > k_largest:
            end = p - 1
        else:
            start = p + 1
    return res

if __name__ == '__main__':
    s="  5.5  /2 + 3*(4/8 -2)  "
    print("-----------Input-----------")
    print(s)
    result = postfix.calculate(s)
    print("-----------Result-----------")
    print(result)
