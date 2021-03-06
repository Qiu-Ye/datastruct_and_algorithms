# -*- coding: utf-8 -*-

"""题目描述
八皇后问题
国际象棋棋盘上有8*8个格子。现在有8枚皇后棋子，一个格子只能放一个棋子，求解所有放法，使得这些棋子不同行、不同列、且不在对角线上（(4,5)和(5,6)就是在对角线上的情况，不合法）。
"""

class Solution(object):
    def __init__(self):
        self.res = 0

    def dfs(self, n, cur, A, visit):
        # curr 代表当前行
        if cur == n:
            print(A)
            self.res += 1
        for col in range(n):
            if not visit[col]:   # 保证了不同列
                flag = True
                # 检测冲突
                for row in range(cur):
                    if cur == row or abs(cur-row) == abs(col-A[row]):
                        # 同行 or 同45度对角线
                        flag = False
                        break
                if flag:
                    visit[col] = True
                    A[cur] = col
                    self.dfs(n, cur+1, A, visit)
                    visit[col] = False


    def nqueen(self, n):
        visit = [False] * n
        tmp = [None] * n
        self.dfs(n, 0, tmp, visit)
        return self.res

if __name__ == '__main__':
    s = Solution()
    res = s.nqueen(8)
    print(res)

