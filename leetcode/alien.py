#
# 现有一种使用英语字母的火星语言，这门语言的字母顺序与英语顺序不同。
#
# 给你一个字符串列表 words ，作为这门语言的词典，words 中的字符串已经 按这门新语言的字母顺序进行了排序 。
#
# 请你根据该词典还原出此语言中已知的字母顺序，并 按字母递增顺序 排列。若不存在合法字母顺序，返回 "" 。若存在多种可能的合法字母顺序，返回其中 任意一种 顺序即可。
#
# 字符串 s 字典顺序小于 字符串 t 有两种情况：
#
# 在第一个不同字母处，如果 s 中的字母在这门外星语言的字母顺序中位于 t 中字母之前，那么 s 的字典顺序小于 t 。
# 如果前面 min(s.length, t.length) 字母都相同，那么 s.length < t.length 时，s 的字典顺序也小于 t 。
import collections
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = collections.defaultdict(list)
        indegree = collections.Counter({c:0 for word in words for c in word})

        for fi,se in zip(words,words[1:]):
            for c,d in zip(fi,se):
                if c!=d and d not in graph[c]:
                    graph[c].append(d)
                    indegree[d] += 1
            else:
                # se is not a prefix of fi
                if len(fi) > len(se):
                    return ''

        q = collections.deque()
