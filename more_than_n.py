s = [1, 3, 4, 5, 6]
n=int(input())
def more_than_n(s, n):
    null = []
    for i in range(len(s)):
        if n < s[i]:
            null.append(s[i])
    return (null)
print(more_than_n(s, n))
