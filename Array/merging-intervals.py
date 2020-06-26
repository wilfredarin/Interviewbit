#https://www.geeksforgeeks.org/merging-intervals/
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        
        A = []
        for i in intervals:
            A.append([i.start,i.end])
        
        A.sort()
        n = len(A)
        stack =  [A[0]]
        for i in range(n):
            pre = stack.pop()
            a = pre[0]
            b = pre[1]
            cur = A[i]
            c = cur[0]
            d = cur[1]
            if a<=c and c<=b:
                if d<=b:
                    stack.append([a,b])
                else:
                    stack.append([a,d])
            else:
                stack.append(pre)
                stack.append(cur)
        ans = []
        for i in stack:    
            ans.append(Interval(i[0],i[1]))
        return ans 
            
        
