#https://www.interviewbit.com/problems/best-time-to-buy-and-sell-stocks-i/
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A)<2:
            return 0
        stack = [A[0]]
        ans = 0
        for i in range(1,len(A)):
            if A[i] >= stack[-1]:
                stack.append(A[i])
            else:
                ans = max(ans,stack[-1]-stack[0])
                while stack and stack[-1]>A[i]:
                    stack.pop()
                stack.append(A[i])
        if stack:
            ans = max(ans,stack[-1]-stack[0])
        return ans
