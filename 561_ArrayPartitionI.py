class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        i = 0
        while i < len(nums):
            result += nums[i]
            i+=2
        return result

def main():
    solution = Solution()
    nums = [1,4,3,2]
    result = solution.arrayPairSum(nums)
    print result

if __name__ == "__main__":
    main()
