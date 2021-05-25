# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
#
# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
#
# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
#
#  
#
# 示例 1：
#
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：true
# 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
# 示例 2：
#
# 输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
# 输出：false
# 解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course in prerequisites:
            prev_c, next_c = course[0],course[1]
            graph[prev_c].append(next_c)

        seen = set()

        for cur in range(numCourses):
            if self.isCycle(cur,graph,seen):
                return False
        return True

    def isCycle(self,cur,graph,seen):

        if cur in seen:
            return True
        seen.add(cur)
        for nei in graph[cur]:
            if self.isCycle(nei,graph,seen):
                return True
        seen.pop()
        return False

# 拓扑排序

import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
# 广度优先更好理解
        graph = collections.defaultdict()
        indegree = [0]*numCourses

        for info in prerequisites:
            prev_course, last_course = info[0],info[1]
            graph[prev_course].append(last_course)
            indegree[last_course] += 1

        q = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        res = []
        while q:
            nodes = q.popleft()
            if indegree[nodes] == 0:
                res.append(nodes)
            for nei in graph[nodes]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return res if not len(q) else []

# 飞机问题
# 有 n 个城市通过 m 个航班连接。每个航班都从城市 u 开始，以价格 w 抵达 v。
#
# 现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到从 src 到 dst 最多经过 k 站中转的最便宜的价格。 如果没有这样的路线，则输出 -1。

# dfs深度遍历简单

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # 遍历这个表且有路径
        price = float('inf')
        graph = [[-1] * n for _ in range(n)]
        visited = [False] * n
        for u, v, w in flights:
            graph[u][v] = w

        def dfs(src, dst, cost, graph, cnt):
            nonlocal price

            if src == dst:
                price = min(cost, price)
                return
            if cnt < 0 or cost > price:
                return
            visited[src] = True
            for i in range(n):
                if graph[src][i] != -1 and visited[i] == False:
                    dfs(i, dst, cost + graph[src][i], graph, cnt - 1)
            visited[src] = False

        dfs(src, dst, 0, graph, K)
        return price if price != float('inf') else -1




















