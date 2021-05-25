# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
#
#  
# 示例 1：
#
# 输入：s = "aa" p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s),len(p)
        mat = [[False] * (n+1) for _ in range(m+1)]
        mat[0][0] = True
        for i in range(m+1):
            for j in range(1,n+1):
                if p[j-1] != '*':
                    if s[i] == p[j-1]:
                        mat[i][j] = mat[i-1][j-1]
                    else:
                        return False
                else:
                    if not self.matches(s[i],p[j-1]):
                        # 这个才对应j - 2，记住字符永远是相对的
                        mat[i][j] = mat[i][j-2]
                    else:
                        mat[i][j] = mat[i][j-2] or mat[i-1][j]

    def matches(self, s, p):
        if s == p or p == '.':
            return True
        return False





