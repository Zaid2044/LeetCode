"""
3330. Find the Original Typed String I (Easy)
LeetCode: https://leetcode.com/problems/find-the-original-typed-string-i/

Alice is attempting to type a specific string on her computer. However, she may press a key for too long, 
resulting in a character being typed multiple times. She may have done this at most once.

You are given a string `word`, which represents the final output displayed on Alice's screen.

Return the total number of possible original strings that Alice might have intended to type.

Example 1:
Input: word = "abbcccc"
Output: 5
Explanation: The possible strings are: "abbcccc", "abbccc", "abbcc", "abbc", "abcccc"

Example 2:
Input: word = "abcd"
Output: 1
Explanation: Only possible string is "abcd"

Example 3:
Input: word = "aaaa"
Output: 4
Explanation: Possible strings are: "aaaa", "aaa", "aa", "a"
"""

def possibleStringCount(word):
    """
    Counts how many possible original strings could result in the typed string `word`
    if Alice long-pressed at most one character.

    The logic:
    - For each group of repeating characters, only one of them is original.
    - All others could be explained as long-presses.
    - So the number of original strings = number of repeating groups in the string.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        word (str): The string shown on screen after typing.

    Returns:
        int: Number of possible original strings.
    """
    count = len(word)
    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            count -= 1
    return count

# Example usage:
# print(possibleStringCount("abbcccc"))  # Output: 5
