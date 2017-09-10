class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flower_len = len(flowerbed)
        flowerbed.append(0)
        flowerbed.insert(0, 0)
        for i in range(1, flower_len + 1):
            print i, flowerbed[i]
            if (flowerbed[i] == 0) and (flowerbed[i + 1] == 0) and (flowerbed[i - 1] == 0):
                n = n - 1
                flowerbed[i] = 1
        return n <= 0

def main():
    solution = Solution()
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    print solution.canPlaceFlowers(flowerbed, n)

if __name__ == "__main__":
    main()
