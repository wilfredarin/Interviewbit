"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example :

Given numerator = 1, denominator = 2, return "0.5"
Given numerator = 2, denominator = 1, return "2"
Given numerator = 2, denominator = 3, return "0.(6)"
"""
def fractionToDecimal(self, A, B):
        if A==0:
            return "0"
        ans = ""
        sign = A*B<0
        A = abs(A)
        B = abs(B)
        integer = A//B
        if sign:
            ans+="-"
        ans+=str(integer)
        res="."
        remainder = A%B
        if not remainder:
            return ans
        hash_table = {}
        while remainder!=0:
            if remainder in hash_table:
                index = hash_table[remainder]
                ans+=res[:index]
                ans+="("
                ans+=res[index:]+")"
                return ans
            else:
                hash_table[remainder] = len(res)
            remainder = remainder*10
            res+=str(remainder//B)
            remainder = remainder%B
        return ans+res
