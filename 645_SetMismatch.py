class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        diff = sum(nums) - (n + 1) * n / 2
        total = 0
        for num in nums:
            total += num * num
        total -= n * (n + 1) * (2 * n + 1) / 6
        total = int(total / diff)
        return [int((total + diff) / 2), int((total - diff) / 2)]

def main():
    solution = Solution()
    nums = [2, 1, 2, 4]
    print(solution.findErrorNums(nums))

if __name__=="__main__":
    main()