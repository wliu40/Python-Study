
def inputArray():
    arr = []
    n = int(raw_input('Enter how many elements you want: '))
    for i in range(0, n):
        x = raw_input('Enter the numbers into the array: ')
        arr.append(int(x))
    return arr

def mergesort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) / 2
        left  = mergesort(arr[:mid])
        right = mergesort(arr[mid:])

        left_cnt, right_cnt, arr_cnt = 0, 0, 0
        while left_cnt < len(left) and right_cnt < len(right):
            if left[left_cnt] < right[right_cnt]:
                arr[arr_cnt] = left[left_cnt]
                left_cnt += 1
            else:
                arr[arr_cnt] = right[right_cnt]
                right_cnt += 1
            arr_cnt += 1

        while left_cnt < len(left):
            arr[arr_cnt] = left[left_cnt]
            left_cnt += 1; arr_cnt += 1

        while right_cnt < len(right):
            arr[arr_cnt] = right[right_cnt]
            right_cnt += 1; arr_cnt += 1
            
        return arr
    
def main():
    arr = []
    arr = inputArray()    
    print arr
    mergesort(arr)
    print arr
