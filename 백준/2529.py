import sys

k = int(sys.stdin.readline())

arr = list(map(str, sys.stdin.readline().strip().split(' ')))

num_min = 9999999999
num_max = -9999999999
str_min = ""
str_max = ""
num = k+1

def brute_force(lv, array):
    global str_min
    global str_max
    global num_min
    global num_max
    if len(array) == num:
        tmp = int("".join(map(str, array)))
        st = "".join(map(str, array))
        if tmp < num_min:
            num_min = tmp
            str_min = st
        if tmp > num_max:
            num_max = tmp
            str_max = st
        # print(f'min: {str_min}, max: {str_max}')
        return

    for i in range(0, 10):
        if lv == 1:
            array.append(i)
            brute_force(lv+1, array)
            array.pop()
        else:
            if i not in array:
                if arr[lv-2] == "<":
                    if array[lv-2] < i:
                        array.append(i)
                        brute_force(lv+1, array)
                        array.pop()
                else:
                    if array[lv-2] > i:
                        array.append(i)
                        brute_force(lv+1, array)
                        array.pop()

brute_force(1, [])

print(str_max)
print(str_min)
