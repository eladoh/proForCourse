
arr = []
for i in range(1,101):
    arr.append(i)
sumOf100 = sum(arr)

missingNumArr = []
for i in range(1,101):
    missingNumArr.append(i)

missingNumArr.pop(8)

result = sumOf100 - sum(missingNumArr)

print(result)