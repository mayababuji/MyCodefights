import itertools
a = [[1,2,3,0],[1,0,5,6],[1,2,3,4]]
#print list(enumerate(a))
for (i,s) in list(enumerate(a)):
    #if s == 0:
    for i in s:
        print i
# for x,y,z in zip(a, itertools.islice(a, 1, None)):
#     for i in range(len(x)):
#         for j in range(len(y)):
#             for k in range(len(z)):
#                 if i == j == k and x[i] == 0:
#                     #y[j] =y[j].append(0)
#                     y[j] = 0
#                     z[k] = 0
#                     print a
#                 
                
                
        #print x[i]
    ##print y



