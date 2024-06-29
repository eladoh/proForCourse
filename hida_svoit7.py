

arr = [1,2 ,3 ,4, -10 ,9 ,10 ,-4,]

def higest_sequence(arr):
    
    higest_sequence_sum = arr[0]
    sequence_sum = arr[0]

    for i in range(0, len(arr)):
        for x in range(0, len(arr)):
            sequence_sum = sum(arr[i:x])

            if sequence_sum > higest_sequence_sum:
                higest_sequence_sum = sequence_sum

    return higest_sequence_sum

print(higest_sequence(arr))
        
        
        
        
