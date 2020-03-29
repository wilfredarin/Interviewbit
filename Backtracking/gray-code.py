
def grayCode(self, n):
    gray_seq = [0, 1]           #gray code for n=1
    for i in range(1,n):        #recursivley extending for n>1
        gray_seq += [s+2**i for s in reversed(gray_seq)]

    return gray_seq

class Solution:
    
    # @param A : integer
    # @return a list of integers
  def grayCode(self, A):
      l1 = ["0","1"]
      l2 = []
      ans = []
      temp = []
      def c(binary):
          take = binary[::-1]
          ans = 0
          for i in range(len(take)):
              ans+=(2**i)*(int(take[i]))
          return ans
      for i in range(A-1):
          l2 = copy.copy(l1)
          l2.reverse()
          temp = []
          for e in range(len(l1)):
              l1[e] ="0"+l1[e]
          for f in range(len(l1)):
              l2[f] = "1"+l2[f]
          l1 = l1 + l2
      for e in l1:
          temp.append(c(e))
      return temp
            
            
                
