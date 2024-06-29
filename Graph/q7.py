"""
Given a weighted, undirected and connected graph of V vertices and an adjacency list adj where adj[i] is a list of lists containing two integers where the first integer of each list j denotes there is edge between i and j , second integers corresponds to the weight of that  edge . You are given the source vertex S and You to Find the shortest distance of all the vertex's from the source vertex S. You have to return a list of integers denoting shortest distance between each node and Source vertex S.
 

Note: The Graph doesn't contain any negative weight cycle.

 

Example 1:

Input:
V = 2
adj [] = {{{1, 9}}, {{0, 9}}}
S = 0
Output:
0 9
Explanation:

The source vertex is 0. Hence, the shortest 
distance of node 0 is 0 and the shortest 
distance from node 1 is 9.
 

Example 2:

Input:
V = 3, E = 3
adj = {{{1, 1}, {2, 6}}, {{2, 3}, {0, 1}}, {{1, 3}, {0, 6}}}
S = 2
Output:
4 3 0
Explanation:

For nodes 2 to 0, we can follow the path-
2-1-0. This has a distance of 1+3 = 4,
whereas the path 2-0 has a distance of 6. So,
the Shortest path from 2 to 0 is 4.
The shortest distance from 0 to 1 is 1 .
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function dijkstra()  which takes the number of vertices V and an adjacency list adj as input parameters and Source vertex S returns a list of integers, where ith integer denotes the shortest distance of the ith node from the Source node. Here adj[i] contains a list of lists containing two integers where the first integer j denotes that there is an edge between i and j and the second integer w denotes that the weight between edge i and j is w.

 

Expected Time Complexity: O(V2).
Expected Auxiliary Space: O(V2).
"""

import heapq

class Solution:
    def dijkstra(self, V, adj, S):
        # Step 1: Initialize distances
        dist = [float('inf')] * V
        dist[S] = 0
        
        # Min-heap priority queue
        pq = [(0, S)]  # (distance, vertex)
        heapq.heapify(pq)
        
        # Step 2: Process vertices using Dijkstra's algorithm
        while pq:
            d, u = heapq.heappop(pq)
            
            # If current distance is greater than known shortest distance, skip
            if d > dist[u]:
                continue
            
            # Explore neighbors
            for v, weight in adj[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
        
        return dist

# Driver Code
if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()
    
    test_cases = int(data[0])
    idx = 1
    
    for _ in range(test_cases):
        V = int(data[idx])
        E = int(data[idx + 1])
        idx += 2
        
        adj = [[] for _ in range(V)]
        for _ in range(E):
            u = int(data[idx])
            v = int(data[idx + 1])
            w = int(data[idx + 2])
            adj[u].append((v, w))
            adj[v].append((u, w))
            idx += 3
        
        S = int(data[idx])
        idx += 1
        
        obj = Solution()
        result = obj.dijkstra(V, adj, S)
        
        for distance in result:
            print(distance, end=" ")
        print()
