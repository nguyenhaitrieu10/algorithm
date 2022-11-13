from collections import deque
import math

class Node():
    def __init__(self, value = -1):
        self.value = value
        self.left = None
        self.right = None

def postorderTraversal(root):
    if not root:
        return []

    s = [root]

    while s != []:
        cur = s[-1]
        if not cur.left and not cur.right:
            s.pop()
            print(cur.value)

        if cur.right:
            s.append(cur.right)
            cur.right = None

        if cur.left:
            s.append(cur.left)
            cur.left = None


def inorderTraversal(root):
    if root is None:
        return True

    stack = []
    node = root
    while stack != [] or node is not None:
        while node is not None:
            stack.append(node)
            node = node.left

        node = stack.pop()
        print(node.value)

        node = node.right

    return True


def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    stack = [root, root]
    while stack:
        node1 = stack.pop()
        node2 = stack.pop()
        if node1 is None and node2 is None:
            continue
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False
        stack.append(node1.left)
        stack.append(node2.right)
        stack.append(node1.right)
        stack.append(node2.left)
    return True

def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    queue = deque()
    queue.append((root, 0))
    result = []
    current_level = 0
    list_node = []
    while queue:
        node, level = queue.popleft()
        if node is None:
            continue
        if level == current_level:
            list_node.append(node.val)
        else:  # level > current_level
            result.append(list_node)
            list_node = [node.val]
            current_level = level

        queue.append((node.left, level + 1))
        queue.append((node.right, level + 1))

    if list_node != []:
        result.append(list_node)

    return result

def insertToTree(root, value):
    if root.val < value:
        if root.right is None:
            root.right = TreeNode(value)
        else:
            insertToTree(root.right, value)
    else:
        if root.left is None:
            root.left = TreeNode(value)
        else:
            insertToTree(root.left, value)

def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """

    def _sortArrayToBST(left, right):
        if left > right:
            return None

        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = _sortArrayToBST(left, mid - 1)
        root.right = _sortArrayToBST(mid + 1, right)
        return root

    return _sortArrayToBST(0, len(nums) - 1)

def merge_2_sorted_array(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    p = m + n - 1
    p1 = m - 1
    p2 = n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[p] = nums1[p1]
            p -= 1
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1
    while p1 >= 0:
        nums1[p] = nums1[p1]
        p -= 1
        p1 -= 1
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p -= 1
        p2 -= 1

def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """

    def _firstBadVersion(left, right):
        while left < right:
            version = (left + right) // 2
            if isBadVersion(version):
                right = version
            else:
                left = version + 1

        return left

    return _firstBadVersion(1, n)

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    current_value = nums[0]
    max_value = nums[0]
    for i in range(1, len(nums)):
        if current_value < 0:
            current_value = nums[i]
        else:
            current_value = current_value + nums[i]
        max_value = max(max_value, current_value)
    return max_value

def maxSubArray(nums: List[int]) -> int:
    def findBestSubarray(nums, left, right):
        # Base case - empty array.
        if left > right:
            return -math.inf

        mid = (left + right) // 2
        curr = best_left_sum = best_right_sum = 0

        # Iterate from the middle to the beginning.
        for i in range(mid - 1, left - 1, -1):
            curr += nums[i]
            best_left_sum = max(best_left_sum, curr)

        # Reset curr and iterate from the middle to the end.
        curr = 0
        for i in range(mid + 1, right + 1):
            curr += nums[i]
            best_right_sum = max(best_right_sum, curr)

        # The best_combined_sum uses the middle element and
        # the best possible sum from each half.
        best_combined_sum = nums[mid] + best_left_sum + best_right_sum

        # Find the best subarray possible from both halves.
        left_half = findBestSubarray(nums, left, mid - 1)
        right_half = findBestSubarray(nums, mid + 1, right)

        # The largest of the 3 is the answer for any given input array.
        return max(best_combined_sum, left_half, right_half)

    # Our helper function is designed to solve this problem for
    # any array - so just call it using the entire input!
    return findBestSubarray(nums, 0, len(nums) - 1)

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.common_root = None

        def recurse_search(node):
            if node is None:
                return False

            mid = False
            if node == p or node == q:
                mid = True

            left = recurse_search(node.left)
            right = recurse_search(node.right)

            if mid + left + right >= 2:
                self.common_root = node
                return True

            return mid or left or right

        recurse_search(root)
        return self.common_root