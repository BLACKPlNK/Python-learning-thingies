import numpy
def biggestSubsequence(A,B):
    x = []   
    for i in range(len(A)):
        x.append([])
        for j in range(len(B)):
            x[i].append(0)
    for i in range(len(A)):
        for j in range(i, len(B)):
            if (j == i):
                for r in range(j, len(A)): 
                    meme2 = 0
                    scream2 = 0
                    if (r > 0):  
                        meme2 = x[r - 1][j]
                    if (j > 0): 
                        scream2 = x[r][j - 1]
                    maxval = max(meme2, scream2)
                    if (A[r] == B[j]):
                        for w in range(r,len(A)):
                            x[w][j] = maxval + 1
                        break
                    else:
                        x[r][j] = maxval
            meme = 0
            scream = 0
            if (i > 0):  
                meme = x[i - 1][j]
            if (j > 0): 
                scream = x[i][j - 1]
            maxval2 = max(meme, scream)
            if (A[i] == B[j]):
                for z in range(j, len(B)):
                    x[i][z] = maxval2 + 1
                break
            else:
                x[i][j] = maxval2
    print x[len(A) - 1][len(B) - 1]
    print (numpy.matrix(x))



biggestSubsequence([2,3,1,2,3], [1,2,3,4])

biggestSubsequence([1,2,3,4], [2,3,1,2,3])
