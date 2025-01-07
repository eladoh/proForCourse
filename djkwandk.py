



# numbers = list(range(1,101))

# numbers.remove(57)


# def Find_missing_number(numbers):

    # needed_sum = sum(range(1,101))
    
    # current_sum = sum(numbers) 
    
    # return abs(needed_sum - current_sum)

    #return [n for n in range(1,101) if n not in numbers][0]
# print(Find_missing_number(numbers))


# numbers = [2, 4, 3, 5, 7, 8, 9]
# target_sum = 10

# כתוב קוד שמוצא את כל הזוגות שסכומם הוא target_sum

# def Find_sum_to_10(numbers, target_sum):
    
#     pairs = []
#     seen = set()

    # for i in range(len(numbers)):
    #     for j in range(i + 1, len(numbers)):
    #         if numbers[i] + numbers[j] == target_sum:
    #             pairs.append((numbers[i],numbers[j]))
            
        
    # return pairs

#     for num in numbers:
#         complament = target_sum - num
#         if complament in seen:
#             pairs.append((complament, num))
#         seen.add(num)

#     return pairs


# pairs = Find_sum_to_10(numbers, target_sum)

# print(pairs)


# numbers = [5, 3, 8, 4, 2, 1, 23, 5]

# def more_then_once(lst):
#     seen = set()

#     for num in numbers:
#         if num not in seen:
#             seen.add(num)
#         else:
#             return num 
#     return None
# # כתוב קוד שמוצא את המספר הראשון שמופיע יותר מפעם אחת
# first_repeated = more_then_once(numbers)
# print(first_repeated)



# def fibonacci(n):

#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
    
#     return fibonacci(n - 1) + fibonacci(n - 2)

# n = 10
# print(fibonacci(n))  # צפה לתוצאה: 55

# def is_anagram(word1, word2):
    
#     l = sorted(list(word1)) # sorted הופך לליסט בכל מקרה
    
#     s = sorted(list(word2))

#     if s == l:
#         return True
#     return False
    


# print(is_anagram("listen", "silent"))  # צפה לתוצאה: True
# print(is_anagram("python", "typhon"))  # צפה לתוצאה: True
# print(is_anagram("hello", "world"))   # צפה לתוצאה: False


# lambda 


# # filter
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# print(list(filter(lambda num: num % 2 ==0 ,numbers)))

# # list comprahintion 

# print([n for n in numbers if n %2 == 0])

#map 

# numbers = [1, 2, 3, 4, 5]


# print(list(map( lambda x: x * x, numbers)))


# עושה את הפעולה של הפונקציה על כל האיברים ברשימה
# from functools import reduce

# numbers = [1, 2, 3, 4, 5]

# print(reduce(lambda x, y: x + y , numbers)) 

# students = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "Diana": 90
# }

# more_then_80 = {}

# for key, value in students.items():
#     if value > 80:
#         more_then_80[key] = value

# #more_than_80 = {key: value for key, value in students.items() if value > 80} # dict comprahanition

# print(more_then_80)

# image_data = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19\x12\83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00?\x00\xf1z(\xab\xb0\xe9Ww\x16b\xea\x04\x12&\xed\xa5P\xe5\x97\xea*\xa3\tM\xda*\xe4N\xa4`\xaf\'b\x95\x15\xd7\xe8:6\x9e\x97\xf0Z\xea\x01\'\x9e\xe07\xee\xf3\xf7@R{t\xe9\xd7\xf2\xac?\x10\xd8C\xa6k\xb7V\x96\xfb\xbc\xa4*T1\xc9\x00\xa88\xfdkz\x98Y\xd3\xa6\xa7/OC\x9e\x962\x9dZ\xae\x9co\xb5\xef\xd1\xad\xb43(\xa2\xb4t\xfd(^\xd9\xdc]\xcb\x7fkg\x04\x12G\x19i\xc4\x87s8r\x00\x08\x8cz#u\xc5s\x1dfu\x15\xa3\x0e\x97\xe7X\\\\\xef\x95<\x9bAs\x87\x8b\x01\xff\x00~\xb1aNy\x1f6wz\x821\xc6j\xb5\xc6\x9f{g\x0c\x13\\\xda\\A\x15\xc2\xee\x85\xe5\x8c\xaa\xc889RG#\x91\xd3\xd4P\x05z(\xab\x1a}\x94\x9a\x8e\xa5kc\x0b"\xcbs2B\x85\xce\x14\x16 \x0c\xe3\xb74\x01^\x8a\xbdq\xa7"M\x046w\xd6\xfa\x8c\xb36\xd5KX\xe5\xdc\x0f\x00\x0c:.I\xcf\x18\xcdX\x97A\xb8\xb5\xb5\x8aK\xb8\xae\xa1\x9d\xe4\xb8F\xb7\xfb9\xde\x9e\\I $\x12\x0e\x08\x90d\xf6\x00\x9ezP\x06M\x15\xa3\xabhz\x8e\x87,I\x7fk,>lj\xe8\xcf\x1b(l\xaa\xb1\x03 r\xbb\x80#\xb1\xe2\xb3\xa8\x00\xa2\xad\xe9\xfa{_\xbc\xbf\xbe\x8a\x08a\x8f\xcc\x9aiwm\x8dw\x05\x04\x85\x05\x8eY\x94p\x0f_L\x911\xd1n\xe5\xd4^\xcbO_\xedGX\xd6M\xd6\x08\xf2\x02\xa4\x03\x9c`\x11\x8d\xc0\x1c\x81\x83\xc5\x00gQW\x86\x99#\xe9\xb6w0\xef\x96[\xab'

# # Save the image
# with open("image.jpg", "wb") as f:
#     f.write(image_data)
import pyperclip

# Get text from clipboard
clipboard_text = pyperclip.paste()

print("Clipboard Text:", clipboard_text)