"""
You are given a connected undirected graph. Perform a Depth First Traversal of the graph.
Note: Use the recursive approach to find the DFS traversal of the graph starting from the 0th vertex from left to right according to the graph.


Example 1:

Input: V = 5 , adj = [[2,3,1] , [0], [0,4], [0], [2]]

Output: 0 2 4 3 1
Explanation: 
0 is connected to 2, 3, 1.
1 is connected to 0.
2 is connected to 0 and 4.
3 is connected to 0.
4 is connected to 2.
so starting from 0, it will go to 2 then 4,
and then 3 and 1.
Thus dfs will be 0 2 4 3 1.
Example 2:

Input: V = 4, adj = [[1,3], [2,0], [1], [0]]

Output: 0 1 2 3
Explanation:
0 is connected to 1 , 3.
1 is connected to 0, 2. 
2 is connected to 1.
3 is connected to 0. 
so starting from 0, it will go to 1 then 2
then back to 0 then 0 to 3
thus dfs will be 0 1 2 3. 

Your task:
You don't need to read input or print anything. Your task is to complete the function dfsOfGraph() which takes the integer V denoting the number of vertices and adjacency list as input parameters and returns a list containing the DFS traversal of the graph starting from the 0th vertex from left to right according to the graph.


Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)


Constraints:
1 ≤ V, E ≤ 104
"""

from typing import List

class Solution:
    
    # Function to perform DFS traversal recursively.
    def dfs(self, node: int, adj: List[List[int]], visited: List[bool], result: List[int]):
        # Mark the current node as visited and add it to the result list.
        visited[node] = True
        result.append(node)
        
        # Visit all adjacent nodes that have not been visited yet.
        for neighbour in adj[node]:
            if not visited[neighbour]:
                self.dfs(neighbour, adj, visited, result)
    
    # Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        visited = [False] * V
        result = []
        
        # Start DFS from node 0
        self.dfs(0, adj, visited, result)
        
        return result

# { 
# Driver Code Starts

if __name__ == '__main__':
    T = int(input())
    while T > 0:
        V, E = map(int, input().split())
        adj = [[] for _ in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob = Solution()
        ans = ob.dfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
        T -= 1

# } Driver Code Ends
