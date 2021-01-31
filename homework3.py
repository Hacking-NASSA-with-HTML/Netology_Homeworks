arr = ["python", "c++", "c", "scala", "java"]


def find_the_letter(arr, letter):
    counter = 0
    for x in range(0, len(arr)):
        for y in range(0, len(arr[x])):
            if letter == arr[x][y]:
                counter = counter + 1
    print(f"В этом списке {counter} {letter}")


find_the_letter(arr, "y")
