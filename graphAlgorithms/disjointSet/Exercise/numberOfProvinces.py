# There are n cities. Some of them are connected, while some are not. If city a is connected directly
# with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth
# city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.


class Solution:
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        v = n

        root = [i for i in range(n)]
        rank = [1] * n

        def find(x, root):
            while x != root[x]:
                x = root[x]
            return x
        
        def union(x, y, root, rank):
            rootX = find(x, root)
            rootY = find(y, root)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    root[rootX] = rootY
                else:
                    root[rootY] = rootX
                    rank[rootX] += 1
                    
        def connected(x, y, root):
            return find(x, root) == find(y, root)
        
        for i in range(n):
            for j in range(n):
                if(i != j):
                    if(isConnected[i][j] == 1 and connected(i, j, root) == False):
                        union(i,j,root,rank)
                        v -= 1
        return v
        