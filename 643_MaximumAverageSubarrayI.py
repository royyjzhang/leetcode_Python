class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        total = 0
        for i in range(0, k):
            total += nums[i]
        now = total
        for i in range(0, len(nums) - k):
            now = now - nums[i] + nums[i + k]
            if (now > total):
                total = now
        return total / k

def main():
    solution = Solution()
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    print(solution.findMaxAverage(nums, k))

if __name__=="__main__":
    main()