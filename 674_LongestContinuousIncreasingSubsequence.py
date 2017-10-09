class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        result = 0
        for i in range(0, len(nums)):
            if (i == 0) or (nums[i - 1] < nums[i]):
                count += 1
                result = max(count, result)
            else:
                count = 1
        return result

def main():
    solution = Solution()
    nums = [1, 3, 5, 4, 7]
    print(solution.findLengthOfLCIS(nums))

if __name__=="__main__":
    main()