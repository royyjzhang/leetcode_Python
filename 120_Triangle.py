class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        layer=len(triangle)
        dp=triangle[layer-1]
        for i in range(layer-2,-1,-1):
            for j in range(0,i+1):
                dp[j]=min(dp[j],dp[j+1])+triangle[i][j]
        return dp[0]

triangle=[[2],[3,4],[6,5,7],[4,1,8,3]]
solution=Solution()
print solution.minimumTotal(triangle)
