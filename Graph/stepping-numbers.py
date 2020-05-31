#https://www.interviewbit.com/problems/stepping-numbers/
def stepnum(self, A, B):
        def bfs(n,m,i,ans):
            q = [i]
            while q:
                t = q.pop(0)
                if t>=n and t<=m:
                    ans.append(t)
                if t==0 or t>m:
                    return 
                lastD = t%10
                v1 = t*10 + lastD - 1
                v2 = t*10 + lastD + 1
                if lastD==0:
                    q.append(v2)
                elif lastD==9:
                    q.append(v1)
                else:
                    q.append(v1)
                    q.append(v2)
        ans = []
        for i in range(10):
            bfs(A, B, i, ans)
        ans.sort()
        return ans
