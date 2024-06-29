

arr = [1,2 ,3 ,4, -1 ,-2 ,-3 ,-4,]

def higest_sequence(arr, sequence_length):
    
    higest_sequence_sum = 0
    sequence_sum = 0

    for i in range(0, len(arr)):
        sequence_sum = sum(arr[i:i + sequence_length])
        if sequence_sum > higest_sequence_sum:
            higest_sequence_sum = sequence_sum

    return higest_sequence_sum

print(higest_sequence(arr, 2))
        
        
        
        
