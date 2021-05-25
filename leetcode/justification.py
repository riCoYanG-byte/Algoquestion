# 给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
#
# 你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
#
# 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
#
# 文本的最后一行应为左对齐，且单词之间不插入额外的空格。
#
# 说明:
#
# 单词是指由非空格字符组成的字符序列。
# 每个单词的长度大于 0，小于等于 maxWidth。
# 输入单词数组 words 至少包含一个单词。
# 示例:
#
# 输入:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# 输出:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # 先填数字
        cur_len = 0
        # 控制单词数量
        cur_words = []
        res = []
        for w in words:
            if len(cur_len) + len(w)+len(cur_words) <= maxWidth:
                cur_len += len(w)
                cur_words.append(w)
            else:
                res.append(self.process(cur_len,cur_words,maxWidth))
                cur_len,cur_words = len(w), [w]

        # final line
        cur = ''
        for i in range(len(cur_words)-1):
            cur += cur+cur_words[i]+''
        cur += cur_words[-1]
        cur += ''*(maxWidth-len(cur))
        res.append(cur)
        
        return res

    def process(self, cur_len, cur_words,maxWidth):

        sub_ret = ""
        normal_space = (maxWidth - cur_len) // (len(cur_words)-1)
        left_space = normal_space + (cur_len%(len(cur_words)-1))


















