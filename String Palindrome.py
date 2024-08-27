def isPalindrome(s):
    return s == s[::-1]
s = "meghi"
ans = isPalindrome(s)
if ans:
    print("YES")
else:
    print("NO")
