class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        contenthash = {}
        result = []
        for f in paths:
            content = f.split(' ')
            root = content[0]
            for i in range(1, len(content)):
                tmp = content[i].split('(')
                filename = tmp[0]
                context = tmp[1][0:-1]
                if context in contenthash:
                    contenthash[context].append(root + "/" + filename)
                else:
                    contenthash[context] = [root + "/" + filename]
        for context in contenthash:
            if len(contenthash[context]) > 1:
                result.append(contenthash[context])
        return result

def main():
    solution = Solution()
    paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
    print solution.findDuplicate(paths)

if __name__ == "__main__":
    main()
