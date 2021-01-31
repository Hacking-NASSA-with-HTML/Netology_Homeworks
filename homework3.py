arr = ["python", "c++", "c", "scala", "java"]


def find_the_letter(arr, letter):
    counter = 0
    for x in range(0, len(arr)):
        for y in range(0, len(arr[x])):
            if letter == arr[x][y]:
                counter = counter + 1
    print(f"В этом списке {counter} {letter}")


find_the_letter(arr, "y")


# Netology variant

# def count_letter(word_list, letter):
#     result = 0
#     for word in word_list:
#         if letter in word:
#             result += 1
#     return result


# print(count_letter(["python", "c++", "c", "scala", "java"], "c"))
