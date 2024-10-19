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