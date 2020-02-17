class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        def operate(a1,a2,op1):
            a1=int(a1)
            a2=int(a2)
            if op1=="*":
                return a1*a2
            elif op1=="+":
                return a1+a2
            elif op1=="-":
                return a2-a1
            else:
                return a2/a1
        op = ["/","*","-","+"]
        stack = []
        a = 0
        x = 0
        y = 0
        while A:
            a = A.pop(0)
            if a in op:
                x = stack.pop()
                y = stack.pop()
                stack.append(operate(x,y,a))
            else:
                stack.append(a)
        return stack.pop()
                
                
