class Solution:
    def traverse(self, prov: int, visited, isConnected: List[List[int]]):
        visited[prov] = True
        for i in range(0, len(isConnected)):
            if isConnected[prov][i] and not visited[i]:
                self.traverse(i, visited, isConnected)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        count = 0
        visited = [False] * n
        for prov in range(0, n):
            if not visited[prov]:
                self.traverse(prov, visited, isConnected)
                count += 1
        return count