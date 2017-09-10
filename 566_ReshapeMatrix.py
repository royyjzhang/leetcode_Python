class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        result = []
        rows = len(nums)
        if rows == 0:
            return nums
        cols = len(nums[0])
        if cols == 0:
            return nums
        if r * c != rows * cols:
            return nums
        nowr = 0
        nowc = 0
        line = []
        for i in range(0, rows):
            for j in range(0, cols):
                line.append(nums[i][j])
                if (len(line) == c):
                    result.append(list(line))
                    line = []
        return result


def main():
    solution = Solution()
    nums = [[1, 4], [3, 2]]
    r = 4
    c = 1
    result = solution.matrixReshape(nums, r, c)
    print(result)

if __name__ == "__main__":
    main()
