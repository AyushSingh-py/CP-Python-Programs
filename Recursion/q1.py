#given a string calculate the length of longest palindromic substring.
def is_palindrome(s):
    return s == s[::-1]
def long_str(s):
    n = len(s)
    max_len = 0
    start = 0
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if is_palindrome(substring):
                cur = j - i + 1
                if cur > max_len:
                    max_len = cur
                    start= i

    return s[start:start + max_len]
str = "madambca"  
result = long_str(str)
print("Longest palindromic substring:", result)
