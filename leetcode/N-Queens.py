from typing import List

class Solution:
    res :List[List[str]]= []
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = [] # 
        track:List[str] = []
        for i in range(0,n):
            track.append('.' * n)
        self.backtrack(0,track)
        # print(track)
        return self.res

    def backtrack(self,n:int,track:List[str]):
        if n == len(track):
            self.res.append(track[:])
            # print(self.res)
            return
        for i in range(0,len(track)):
            if not self.valide(n,i,track):
                continue
            track[n] = track[n][:i]+'Q'+track[n][i+1:]
            self.backtrack(n+1,track)
            track[n] = track[n][:i]+'.'+track[n][i+1:]

    def valide(self,raw:int,col:int,track:List[int])->bool:
        for i in range(0,len(track)):# col 去检查每一个列
            if track[i][col] == 'Q':
                return False
        q = raw
        p = col
        for i in range(0,raw):
            q = q - 1
            p = p - 1
            if q < 0 or p < 0 : break
            if track[q][p] == 'Q':
                return False
        q = raw
        p = col
        for i in range(0,raw):
            q = q - 1
            p = p + 1
            if q < 0 or p >= len(track) : break
            if track[q][p] == 'Q':
                return False
        return True
            
        





if __name__ == "__main__":
    so = Solution()
    so.solveNQueens(4)