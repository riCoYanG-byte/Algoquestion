from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        arr = []
        n = len(profit)
        for i in range(len(profit)):
            arr.append([startTime[i],endTime[i],profit[i]])

        dp = [0] * (n+1)
        arr = [0,0,0] + arr
        arr.sort(key=lambda x:x[1])

        for i in range(1,n+1):
            left,right = 0,i-1
            ans = -1
            while left <= right:
                mid = (left+right) // 2
                if arr[mid][2] <= arr[i][0]:
                    ans = mid
                    left = mid+1
                else:
                    right = mid-1

            dp[i] = max(dp[i-1],dp[ans]+arr[i][2])

        return dp[-1]


