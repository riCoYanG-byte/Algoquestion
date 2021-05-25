# 给定一组 互不相同 的单词， 找出所有 不同 的索引对 (i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。
#
#  
#
# 示例 1：
#
# 输入：words = ["abcd","dcba","lls","s","sssll"]
# 输出：[[0,1],[1,0],[3,2],[2,4]]
# 解释：可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
# 示例 2：
#
# 输入：words = ["bat","tab","cat"]
# 输出：[[0,1],[1,0]]
# 解释：可拼接成的回文串为 ["battab","tabbat"]
# 示例 3：
#
# 输入：words = ["a",""]
# 输出：[[0,1],[1,0]]
from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ma = {}
        ret = []
        for idx,w in enumerate(words):
            ma[w[::-1]] = idx
        for idx,w in enumerate(words):
            for i in range(len(w)):
                if w[:i+1] in ma and self.isPalindrome(w[i]):
                    ret.append([idx,ma[w[::-1]]])
        return ret

    def isPalindrome(self,s):
        return s == s[::-1]
