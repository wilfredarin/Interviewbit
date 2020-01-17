def repeatedNumber(self, A):
        n = len(A)
        s = (n*(n+1))//2
        square = (s*(2*n+1))//3
        real_s =0
        real_square = 0
        for i in A:
            real_s+=i
            real_square += i*i
        #d = a - b(repeated-not_present)
        #s-a+b=real_s | s-real_s =a-b
        #square-a^2+b^2 = real_sq | square-real_sq = a^2-b^2=c
        #c/d= (a-b)*(a+b)//a-b = a+b
        #d+c//d = 2a | d-c//d = 2b
        d = s - real_s
        c = square - real_square
        ans = [(c//d-d)//2,(d+c//d)//2]
        return ans
