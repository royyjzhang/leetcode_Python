class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        result = ""
        if (len(nums) == 0):
            return result
        elif (len(nums) == 1):
            return str(nums[0])
        elif (len(nums) == 2):
            return str(nums[0]) + "/" + str(nums[1])
        result += str(nums[0]) + "/(" + str(nums[1])
        for i in range(2, len(nums)):
            result += "/" + str(nums[i])
        result += ")"
        return result

def main():
    solution = Solution()
    nums = [1000, 100, 10, 2]
    print solution.optimalDivision(nums)

if __name__ == "__main__":
    main()
