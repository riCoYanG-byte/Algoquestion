class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        cur = trie
        for word in words:
            for w in word:
                if w not in cur:
                    cur[w] = {}
                    cur = cur[w]
                cur = cur[w]
            cur['$'] = word

        ret = []
        def dfs(i, j, parent):
            letter = board[i][j]
            cur = parent[letter]

            if '$' in cur:
                ret.append(cur['$'])


            board[i][j] = '#'
            for d in ((-1,0),(1,0),(0,1),(0,-1)):
                x = i + d[0]
                y = j + d[1]
                if 0<=x<len(board[0]) and 0<=y<len(board):
                    if not board[x][y] in cur:
                        continue
                    dfs(x,y,cur)

            board[i][j] = letter




        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    dfs(i,j,trie)
        return ret





