def maxSubArray(self, A):
        max_ending_here = A[0]
        max_so_far = A[0]
        for i in range(1,len(A)):
            max_ending_here = max(max_ending_here+A[i],A[i])
            if max_so_far<max_ending_here:
                max_so_far = max_ending_here
        return max_so_far
