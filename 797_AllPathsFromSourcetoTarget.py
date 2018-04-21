class Solution:
    def __init__(self):
        self.result = []

    def findPath(self, current, visited, path, graph):
        if (current == len(graph) - 1):
            self.result.append(list(path))
        next_node = graph[current]
        for node in next_node:
            if node not in visited:
                visited.add(node)
                path.append(node)
                self.findPath(node, visited, path, graph)
                visited.remove(node)
                path.remove(node)

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.findPath(0, set([0]), [0], graph)
        return self.result
        
def main():
    solution = Solution()
    graph = [[1, 2], [3], [3], []]
    print(solution.allPathsSourceTarget(graph))

if __name__ == "__main__":
    main()
