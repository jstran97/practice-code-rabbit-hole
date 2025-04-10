"""
Input:
    Two strings, s and t

Output:
    True if s is subsequence of t
        Subsequence = new string formed from original string by deleting some (or none) of characters without disturbing positions of remaining characters

Restriction(s):
"""

def isSubsequence(s, t):

    if len(s) > len(t):
        return False
    if len(s) == 0:
        return True
    
    subsequence = 0

    for index in range(0, len(t)):
        if subsequence <= len(s) - 1:
            print(f's[subsequence]: {s[subsequence]}')
            print(f't[index]: {t[index]}')
            # If char in string "s" matches that in string "t", move to next char in "s"
            if s[subsequence] == t[index]:
                subsequence += 1

    print(f's: {s}')
    print(f't: {t}')
    print(f'subsequence: {subsequence}')

    # If each char in string "s" found a match in string "t", return True
    return subsequence == len(s)




print(isSubsequence("sal", "small"))