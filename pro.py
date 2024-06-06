def fromNumTobinery(x):
    bitlist = [128,64,32,16,8,4,2,1]
    returnList = []
    for y in bitlist:
        if(x >= y):
            x = x - y
            returnList.append(1)
        else:
            returnList.append(0)
    return returnList

def fromBineryToMinus(bineryList):
    result = []
    for i in bineryList:
        if(i == 0):
            i = 1
            result.append(i)
        else:
            i = 0
            result.append(i)
            
    carry = 1;
    result.reverse()
    for i in range(len(result)):
        if(result[i] == 1):
            result[i] = result[i] - carry
        elif(result[i] == 0 and carry == 1):
            result[i] = 1
            carry = 0
    result.reverse()
    return result
    
print(fromNumTobinery(42))

print(fromBineryToMinus(fromNumTobinery(42)))