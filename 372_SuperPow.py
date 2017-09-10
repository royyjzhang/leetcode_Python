class Solution(object):
    def powmod(self,a,k):
        a=a%1337
        result=1
        for i in range(0,k):
            result=(result*a)%1337
        return result
    def superPow(self, a, b):
        if (len(b)==0):
            return 1
        last_dig=b.pop()
        return self.powmod(self.superPow(a,b),10)*self.powmod(a,last_dig)%1337

solution=Solution()
a=2
b=[10]
print solution.superPow(a,b)
