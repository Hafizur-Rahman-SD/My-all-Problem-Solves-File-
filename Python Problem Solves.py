

'''Problem 1: Longest Substring Without Repeating Characters
Problem:
You are given a string. Find the length of the longest part of the string that has all different characters.

Example:
Input: "abcabcbb"
Output: 3
Explanation: The longest part with all different letters is "abc".'''



def longest_unique_substring(s):
    seen = set()
    start = 0
    max_length = 0

    for end in range(len(s)):
        while s[end] in seen:
            seen.remove(s[start])
            start += 1
        seen.add(s[end])
        max_length = max(max_length, end - start + 1)

    return max_length

# Test
print(longest_unique_substring("abcabcbb"))  # Output: 3
