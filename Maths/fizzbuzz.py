def fizzBuzz(self, A):
        n = A
        a = "Fizz"
        b = "Buzz"
        c = "FizzBuzz"
        l = []
        for i in range(1,n+1):
            if i%15==0:
                l.append(c)
            elif i%3==0:
                l.append(a)
            elif i%5==0:
                l.append(b)
            else:
                l.append(i)
        return l
