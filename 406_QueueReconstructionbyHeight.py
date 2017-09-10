class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        height = []
        result = []
        peopleset = {}

        for i in range(0, len(people)):
            person = people[i]
            if person[0] in peopleset:
                peopleset[person[0]].append((person[1], i))
            else:
                peopleset[person[0]] = [(person[1], i)]
                height.append(person[0])

        height.sort()

        for h in height[::-1]:
            peopleset[h].sort()
            for p in peopleset[h]:
                result.insert(p[0], people[p[1]])
        return result

def main():
    solution = Solution()
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print solution.reconstructQueue(people)

if __name__ == "__main__":
    main()
