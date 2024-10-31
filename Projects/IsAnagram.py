def isAnagram(s1, s2):
    d = {}
    d1 = {}
    for i in s1:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1
    for k in s2:
        if k not in d1:
            d1[k] = 1
        else:
            d1[k] = d1[k] + 1
    return d == d1
print(isAnagram("silence", "buy"))
