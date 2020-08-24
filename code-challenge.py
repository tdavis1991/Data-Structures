nums = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

def divides_3(arr):

    for x in arr:
        if x % 3 == 0:
            print(x)


divides_3(nums)