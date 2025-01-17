"""
Given two strings S1 and S2 in lowercase, the task is to make them anagram. The only allowed operation is to remove a character from any string. Find the minimum number of characters to be deleted to make both the strings anagram. Two strings are called anagram of each other if one of them can be converted into another by rearranging its letters.

Example 1:

Input:
S1 = bcadeh
S2 = hea
Output: 3
Explanation: We need to remove b, c
and d from S1.
Example 2:

Input:
S1 = cddgk
S2 = gcd
Output: 2
Explanation: We need to remove d and
k from S1.
Your Task:
Complete the function remAnagram() which takes two strings S1, S2 as input parameter, and returns minimum characters needs to be deleted.

Expected Time Complexity: O(max(|S1|, |S2|)), where |S| = length of string S.
Expected Auxiliary Space: O(26)

Constraints:
1 <= |S1|, |S2| <= 105
"""

def remAnagram(S1, S2):
    # Initialize arrays to count frequency of characters
    count1 = [0] * 26
    count2 = [0] * 26

    # Count frequencies of characters in S1
    for char in S1:
        count1[ord(char) - ord('a')] += 1

    # Count frequencies of characters in S2
    for char in S2:
        count2[ord(char) - ord('a')] += 1

    # Calculate the number of deletions needed
    deletion = 0
    for i in range(26):
        deletion += abs(count1[i] - count2[i])

    return deletion

# Driver code
if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        S1 = input().strip()
        S2 = input().strip()
        print(remAnagram(S1, S2))
