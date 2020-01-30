def countAndSay(self, A):
        dp = ["1","11","21","1211","111221"]
        n = 4
        while n<A:
            dp.append("0")
            n+=1
        if A<=5:
            return dp[A-1]
        for i in range(4,A):
            k = dp[i][0]
            s=""
            c = 0
            t = len(dp[i])
            j = 0
            while j<t:
                if k==dp[i][j]:
                    c+=1
                else:
                    s+=str(c)+k
                    k = dp[i][j]
                    c = 1
                j+=1
            s+=str(c)+k
            dp[i+1]=s   
        return dp[A-1]
