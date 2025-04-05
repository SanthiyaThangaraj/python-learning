'''write a function to find largest common prefix among a list of words
def common_prefix(words):
    if len(words)==0:
        return ""
    prefix=words[0]
    i=0
    while i<len(prefix):
        for word in words:
            if i>=len(word) or word[i]!=prefix[i]:
                return prefix[:1]
        i+=1
        return prefix

words=['apple','applet']
print(common_prefix(words))'''

def common_prefix(words):
    if len(words)==0:
        return ""
    first=words[0]
    last=words[-1]
    i=0
    while(i<len(first) and i<len(last) and first[i]==last[i]):
        i+=1
    return first[:i]

words=['aple','ale',
       'aplet']
print(common_prefix(words))
