"""
Given an integer array coins[ ] of size N representing different denominations of currency and an integer sum, find the number of ways you can make sum by using different combinations from coins[ ].  
Note: Assume that you have an infinite supply of each type of coin. And you can use any coin as many times as you want.

Example 1:

Input:
N = 3, sum = 4
coins = {1,2,3}
Output: 4
Explanation: Four Possible ways are: {1,1,1,1},{1,1,2},{2,2},{1,3}.
Example 2:

Input:
N = 4, Sum = 10
coins = {2,5,3,6}
Output: 5
Explanation: Five Possible ways are: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}.
Your Task:
You don't need to read input or print anything. Your task is to complete the function count() which accepts an array coins its size N and sum as input parameters and returns the number of ways to make change for given sum of money. 

Expected Time Complexity: O(sum*N)
Expected Auxiliary Space: O(sum)

Constraints:
1 <= sum, N, coins[i] <= 103
"""

class Solution:
    def count(self, coins, N, Sum):
        # Initialize a list to store the number of ways to make each amount
        dp = [0] * (Sum + 1)
        dp[0] = 1  # Base case: There is one way to make sum 0
        
        # Iterate over each coin
        for coin in coins:
            # Update the dp array for all sums that can include this coin
            for i in range(coin, Sum + 1):
                dp[i] += dp[i - coin]
        
        return dp[Sum]

#{ 
 # Driver Code Starts
# Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum, N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins, N, sum))

# } Driver Code Ends
