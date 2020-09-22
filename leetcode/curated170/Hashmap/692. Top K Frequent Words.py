# Given a non-empty list of words, return the k most frequent elements.
#
# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
#

import collections


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dicts = collections.Counter(words)
        keys = dicts.keys()
        # 从小到大去排列
        keys.sort(key=lambda w: (-dicts[w], w))
        return keys[:k]


