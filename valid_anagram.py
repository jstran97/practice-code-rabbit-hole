"""
NeetCode

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""

def isAnagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    s_count = {}
    t_count = {}

    for letter in s:
        if letter in s_count:
            s_count[letter] += 1
        else:
            s_count[letter] = 1

    for letter in t:
        if letter in t_count:
            t_count[letter] += 1
        else:
            t_count[letter] = 1

    return s_count == t_count