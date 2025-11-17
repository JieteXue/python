def is_anagram(s, t):
    if len(s) != len(t):
        return False
    s = list(s)
    t = list(t)
    s.sort()
    t.sort()
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
    return True


print(is_anagram('anagram', 'nagaram')) # True
print(is_anagram('anagrm', 'nagaram')) # False
print(is_anagram('rat', 'car')) # False