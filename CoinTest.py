import numpy
def CoinTest(A, B, C): 
    valArray = []
    valArray.append([True, 0])
    for y in range (A):
        valArray.append([False, 999999])
    for z in range (1, A + 1):
        for x in range (len(B)):
            if B[x] <= z: 
                if (valArray[z - B[x]][0] == True and valArray[z - B[x]][1] < valArray[z][1]):
                    valArray[z][0] = True
                    valArray[z][1] = valArray[z - B[x]][1] + 1
    print numpy.matrix(valArray)
    return (valArray[A][0] == True and valArray[A][1] <= C)
print CoinTest(10, [4,5], 5)
        
