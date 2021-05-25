# 归并排序
import random


def merge2lists(left_list, right_list):
    ret = []
    i,j = 0,0
    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            ret.append(left_list[i])
            i += 1
        else:
            ret.append(right_list[j])
            j += 1
    if left_list:
        for c in range(i,len(left_list)):
            ret.append(left_list[c])
    if right_list:
        for c in range(j,len(right_list)):
            ret.append(right_list[c])
    return ret


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = (len(nums) + 1) // 2

    left_list = merge_sort(nums[:mid])
    # 多写个+1
    right_list = merge_sort(nums[mid:])
    return merge2lists(left_list,right_list)

# 快速排序




def quickSort(nums):
    if len(nums) <= 1:
        return nums
    pivot_idx = random.randint(0,len(nums)-1)

    smaller = [s for s in nums if s < nums[pivot_idx]]
    larger = [l for l in nums if l > nums[pivot_idx]]

    return quickSort(smaller) + [nums[pivot_idx]] + quickSort(larger)


if __name__ == '__main__':
    #print(merge_sort([1,3,5,4,6]))
    nums = [1,3,5,4,6]
    print(quickSort(nums))

