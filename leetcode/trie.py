# Trie模板
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.dic
        for wo in word:
            if wo not in cur:
                cur[wo] = {}
            cur = cur[wo]
        cur['end'] = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.dic
        for wo in word:
            if wo not in cur:
                return False
            cur = cur[wo]

        return 'end' in cur


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t = self.dic
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        return True




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)





# auto complete

# Example:



# Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
# The system have already tracked down the following sentences and their corresponding times:
# "i love you" : 5 times
# "island" : 3 times
# "ironman" : 2 times
# "i love leetcode" : 2 times
# Now, the user begins another search:
#
# Operation: input('i')
# Output: ["i love you", "island","i love leetcode"]
# Explanation:
# There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
#
# Operation: input(' ')
# Output: ["i love you","i love leetcode"]
# Explanation:
# There are only two sentences that have prefix "i ".
#
# Operation: input('a')
# Output: []
# Explanation:
# There are no sentences that have prefix "i a".
#
# Operation: input('#')
# Output: []
# Explanation:
# The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.
from typing import List


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = {}
        for i, sentence in enumerate(sentences):
            node = self.trie
            for c in sentence:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["#"] = times[i]
        self.node = self.trie
        self.prefix = []

    def input(self, c: str) -> List[str]:
        if c == "#":
            if "#" in self.node:
                self.node["#"] += 1
            else:
                self.node["#"] = 1
            self.prefix = []
            self.node = self.trie
            return []

        if c not in self.node:
            self.node[c] = {}
        self.node = self.node[c]
        self.prefix.append(c)

        ans = []

        self.dfs(self.node, self.prefix, ans)

        ans.sort(key=lambda x: (-x[0], x[1]))
        return [x[1] for x in ans][:3]

    def dfs(self, node, prefix, ans):
        for k in node:
            if k != "#":
                prefix.append(k)
                self.dfs(node[k], prefix, ans)
                prefix.pop()
            else:
                ans.append([node["#"], "".join(prefix)])

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)