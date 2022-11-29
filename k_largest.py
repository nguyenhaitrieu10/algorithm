import heapq
import random

def findKthLargest(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    return heapq.nlargest(k, nums)[-1]


def partition(start, end, nums):
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


def quick_select(start, end, nums, k_largest):
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


nums = [1,2,3]
k = 2
if k <= len(nums):
    result = quick_select(0, len(nums) - 1, k - 1)
