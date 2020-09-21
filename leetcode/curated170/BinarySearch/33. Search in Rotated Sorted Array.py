# You
# are
# given
# an
# integer
# array
# nums
# sorted in ascending
# order, and an
# integer
# target.
#
# Suppose
# that
# nums is rotated
# at
# some
# pivot
# unknown
# to
# you
# beforehand(i.e., [0, 1, 2, 4, 5, 6, 7]
# might
# become[4, 5, 6, 7, 0, 1, 2]).
#
# If
# target is found in the
# array
# return its
# index, otherwise,
# return -1.
#
# Example
# 1:
#
# Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
# Output: 4
from typing import List

# 判断好顺序就可以进行二分查找因为rotate index 一定是保持部分有序的
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1