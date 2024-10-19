'''
Minimum times A has to be repeated such that B is a substring of it     https://www.geeksforgeeks.org/problems/minimum-times-a-has-to-be-repeated-such-that-b-is-a-substring-of-it--170631/1?page=1&sortBy=submissions
Difficulty: Medium

Given two strings A and B. Find minimum number of times A has to be repeated such that B is a Substring of it. If B can never be a substring then return -1.

Example 1:

Input:
A = "abcd"
B = "cdabcdab"
Output:
3
Explanation:
Repeating A three times (“abcdabcdabcd”),
B is a substring of it. B is not a substring
of A when it is repeated less than 3 times.

Example 2:
Input:
A = "ab"
B = "cab"
Output :
-1
Explanation:
No matter how many times we repeat A, we can't
get a string such that B is a substring of it.

Expected Time Complexity: O(|A| * |B|)
Expected Auxiliary Space: O(|B|)

Constraints:
1 ≤ |A|, |B| ≤ 103
String A and B consists of lower case alphabets
'''
def minRepeats(a,b):
    # Starting with "a" repeated once.
    count=1  
    repeated_a=a   

    # Keep repeating until repeated_A is at least as long as B
    while len(repeated_a)<len(b):
        repeated_a+=a
        count+=1

    # Checking if "b" is a substring of "a"
    if b in repeated_a :
        return count 
    
    # Try adding one more repetition to cover wraparound cases
    repeated_a+=a
    count+=1

    if b in repeated_a :
        return count

    # If B is still not a substring, return -1
    return -1

A = "abcabc"
B = "cab"
print(minRepeats(A,B))