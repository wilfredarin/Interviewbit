def convertToTitle(self, A):
        s=""
        while A:
            d = A%26

            if not d:
                s+="Z"
                A=A//26-1
            else:
                A=A//26
                s+=chr(d+64)
        s = s[::-1]
        return s
