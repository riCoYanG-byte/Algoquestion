# calculator1 只做加减法、用stack去存字符
# 加减法没有顺序

# solution1
class Solution:
    def calculate(self, s: str) -> int:
        opt = [1]
        i = 0
        sign = 1
        res = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
            elif s[i]== '+':
                # 不改变方向
                sign = opt[-1]
                i += 1
            elif s[i] == '-':
                # 改变方向，可以控制--得正
                sign = -opt[-1]
                i += 1
            elif s[i] == '(':
                # 不改辨方向,添加新一轮的计算内容
                opt.append(sign)
                i += 1
            elif s[i] == ')':
                opt.pop()
                i += 1
            else:
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num*10 + ord(s[i]) - ord('0')
                    i += 1
                res += num*sign
        return res

# solution2
# 这个思路很优秀
class Solution:
    def calculate(self, s: str) -> int:
        def dfs(s, start):
            stack = []
            pre_flag = '+'
            num = 0
            i = start
            while i < len(s):
                c = s[i]
                if  c == ' ':
                    i += 1
                    continue
                elif c == '(':
                    i, num = dfs(s, i+1)
                elif c.isdigit():
                    num = num * 10 + int(c)
                else:
                    if pre_flag == '+':
                        stack.append(num)
                    elif pre_flag == '-':
                        stack.append(-num)
                    if c == ')': break
                    pre_flag = c
                    num = 0
                i += 1
            return i, sum(stack)
        s += '$'
        return dfs(s, 0)[1]

# dfs的思路很清晰

 # 带乘除法的用stack去存字符
class Solution:
    def calculate(self, s: str) -> int:

        presign = '+'
        cal = []
        num = 0
        for i, cha in enumerate(s):
            if s[i] != ' ' and s[i].isdigit():
                # 适合处理乘除法，这样的需要判断最后一个边界的
                num = num * 10 + ord(s[i]) - ord('0')

            if i == len(s) - 1 or cha in '+-*/':
                if presign == '+':
                    cal.append(num)
                if presign == '-':
                    cal.append(-num)
                if presign == '*':
                    cal.append(cal.pop() * num)
                if presign == '/':
                    cal.append(int(cal.pop() / num))
                presign = cha
                num = 0

        return sum(cal)

