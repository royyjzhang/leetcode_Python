class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        min_num = arrays[0][0]
        max_num = arrays[0][len(arrays[0]) - 1]
        result = 0
        for i in range(1, len(arrays)):
            result = max(result, abs(arrays[i][0] - max_num))
            result = max(result, abs(arrays[i][len(arrays[i]) - 1] - min_num))
            min_num = min(min_num, arrays[i][0])
            max_num = max(max_num, arrays[i][len(arrays[i]) - 1])
        return result

def main():
    solution = Solution()
    arrays = [[1, 2, 3], [4, 5], [1, 2, 3]]
    print solution.maxDistance(arrays)

if __name__ == "__main__":
    main()
