# 在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.
#
# 一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.
#
# 最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
#
# 给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。
from typing import List

import collections
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        current = []
        for l in board:
            for il in l:
                current.append(il)
        target = [1,2,3,4,5,6]
        q = collections.deque()
        q.append(current)

        C = len(board[0])
        while q:
            cur = q.popleft()
            for d in (-1,1,-C,C):
                 nei = cur.index(0)+d
                 if abs(nei.index(0)/C-cur.index(0)/C) + abs(nei(0)-cur(0)) == 1:
                     continue
                 else:
                     q.append(cur)
