class Solution(object):
    def __init__(self):
        self.count = 0

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def helper(self, nums, start):
        if (start == 0):
            self.count += 1
            return
        for i in range(start, 0, -1):
            self.swap(nums, start, i)
            if (nums[start] % start == 0) or (start % nums[start] == 0):
                self.helper(nums, start - 1)
            self.swap(nums, i, start)

    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if (N == 0):
            return 0
        nums = range(N + 1)
        self.helper(nums, N)
        return self.count

def main():
    solution = Solution()
    N = 8
    print solution.countArrangement(N)

if __name__ == "__main__":
    main()
