class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        s = set()
        for candy in candies:
            s.add(candy)
        return min(int(len(candies) / 2), len(s))

def main():
    solution = Solution()
    candies = [1, 1, 2, 2, 3, 3]
    result = solution.distributeCandies(candies)
    print(result)

if __name__ == "__main__":
    main()
