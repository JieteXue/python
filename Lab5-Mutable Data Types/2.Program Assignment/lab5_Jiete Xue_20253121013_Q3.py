def longest_substring(text):
    l = 0
    start = 0
    seen = {}
    for i, char in enumerate(text):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        else:
            longest = max(l, i - start + 1)
        seen[char] = i
    return l
print(longest_substring("abcabdef")) 
print(longest_substring("aaaaa")) 
print(longest_substring("pwwkew"))