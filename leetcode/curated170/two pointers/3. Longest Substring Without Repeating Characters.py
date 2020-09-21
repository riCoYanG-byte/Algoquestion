# Given a string s, find the length of the longest substring without
# repeating characters.

# 以 \texttt{(a)bcabcbb}(a)bcabcbb 开始的最长字符串为 \texttt{(abc)abcbb}(abc)abcbb；
# 以 \texttt{a(b)cabcbb}a(b)cabcbb 开始的最长字符串为 \texttt{a(bca)bcbb}a(bca)bcbb；
# 以 \texttt{ab(c)abcbb}ab(c)abcbb 开始的最长字符串为 \texttt{ab(cab)cbb}ab(cab)cbb；
# 以 \texttt{abc(a)bcbb}abc(a)bcbb 开始的最长字符串为 \texttt{abc(abc)bb}abc(abc)bb；
# 以 \texttt{abca(b)cbb}abca(b)cbb 开始的最长字符串为 \texttt{abca(bc)bb}abca(bc)bb；
# 以 \texttt{abcab(c)bb}abcab(c)bb 开始的最长字符串为 \texttt{abcab(cb)b}abcab(cb)b；
# 以 \texttt{abcabc(b)b}abcabc(b)b 开始的最长字符串为 \texttt{abcabc(b)b}abcabc(b)b；
# 以 \texttt{abcabcb(b)}abcabcb(b) 开始的最长字符串为 \texttt{abcabcb(b)}abcabcb(b)。


def lengthOfLongestSubstrings(s) :
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        occ.add(s[0])
        n = len(s)-1
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动

        rk, ans = 0, float('-inf')
        for i in range(n):
            while rk < n and s[rk+1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk+1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
            occ.remove(s[i])
        return ans

print(lengthOfLongestSubstrings("abcabcbb"))
