class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        if (n<2):
            return nums
        nums.sort()
        parent=[0 for i in range(0,n)]
        count=[0 for i in range(0,n)]
        maxcount=0;
        maxind=-1;
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if ((nums[j]%nums[i]==0) and (count[i]<count[j]+1)):
                    count[i]=count[j]+1
                    parent[i]=j
                    if (count[i]>maxcount):
                        maxcount=count[i]
                        maxind=i
        result=[0 for i in range(0,maxcount)]
        for i in range(0,maxcount):
            result[i]=nums[maxind]
            maxind=parent[maxind]
        return result

solution=Solution()
nums=[1,2,4,8]
print solution.largestDivisibleSubset(nums)
