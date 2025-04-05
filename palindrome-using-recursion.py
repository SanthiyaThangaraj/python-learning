def palindrome(s):
    if len(s)==1:
        return True
    if len(s)<2:
        return True
    '''elif s[0]!=s[-1]:
        return False'''
    return palindrome(s[1:-1])

s=input("Enter string:")
print(palindrome(s))
