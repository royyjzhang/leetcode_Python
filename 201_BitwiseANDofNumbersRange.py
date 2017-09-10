class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if (m==0):
            return 0
        leftshift=0
        while ((m!=0) and (n!=m)):
            m=m>>1
            n=n>>1
            leftshift+=1
        if (m==0):
            return 0
        else:
            return m<<leftshift

m=5
n=7
solution=Solution()
print solution.rangeBitwiseAnd(m,n)
