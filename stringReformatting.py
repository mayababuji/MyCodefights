#!/usr/bin/env python
#-*-coding : utf-8 -*-

def stringReformatting(s, k):
    s = s.replace("-","")
    str_ln = len(s)- 1
    new_str = []
    i = 0
    while str_ln >= 0:
        if i == k:
            i = 0
            new_str.insert(0,"-")
        new_str.insert(0,s[str_ln])
        i += 1
        str_ln -=1
    return "".join(new_str)
        
        
def sortByString(s, t):
    return "".join(sorted(s,key=t.index))






























# def stringReformatting(s, k):
#     s = s.replace('-','')
#     s_l = len(s) -1
#     #s_l =7
#     i = 0
#     new_str = []
#     while s_l >= 0:
#         if i == k:
#             i = 0
#             new_str.insert(0, '-')
#             print new_str
#         new_str.insert(0, s[s_l])
#         print new_str,"first"
#         #print new_str
#         i += 1
#         s_l -= 1
#     return "".join(new_str)
 
if __name__ == "__main__":
    s = "2-4a0r7-4k"
    k = 2
    print stringReformatting(s, k)

# def stringReformatting(s, k):
#     s = s.replace("-","")
#     c = list(s)
#     c.reverse()
#     n = []
#     for i in range(len(c)):
#         j = i +1
#         print j,k
#         if j == k:
#             n.append("-")
#             k += k
#             print n
#         n.append(c[i])
#     n.reverse()  
#     return "".join(n)
# 
# if __name__ == "__main__":
#     s = "abc-xyz"
#     k = 1
#     print stringReformatting(s, k)
        
    








