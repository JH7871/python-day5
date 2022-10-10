def longestSubstring(s, k, ans):  
    freq = {}
    for i in s:
        freq[i] = freq.get(i,0)+1
        
    flag = False
    for i in s:
        if freq[i]<k:
            flag = True
            new = s.split(i)
            for st in new:
                x = longestSubstring(st,k,ans)
                ans = max(ans,x)
            break
    if not flag:
        ans = max(ans,len(s))
    return ans
s = input("enter the string:")
k = int(input("enter the number:"))
print("output",longestSubstring(s,k,0))
