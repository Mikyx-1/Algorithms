# Implementation of quick select (Variant of quick sort)


def sort_with_pivot(arr, start, end):
    ptr1 = 0
    ptr2 = -1
    pivot = end
    pivot_value = arr[pivot]
    index = pivot
    for i in range(len(arr)):
        if arr[ptr1] > pivot_value:
            pass
        elif arr[ptr1] <= pivot_value:
            ptr2 += 1
            if ptr1 > ptr2:
                arr[ptr1], arr[ptr2] = arr[ptr2], arr[ptr1]
                if i == len(arr) - 1:
                    index = ptr2
            elif ptr1 == ptr2:
                pass
        ptr1 += 1
    return arr, index


def quick_select(arr, start, end, k):

    sorted_arr, idx = sort_with_pivot(arr, start, end)
    if idx == k:
        return arr[idx]
    elif k < idx:
        return quick_select(sorted_arr, start, idx-1, k)
    else:
        return quick_select(sorted_arr, idx+1, end, k)


arr = [3, 2, 0, 1, 5, 8, 7, 6, 9, 4]
print(quick_select(arr, 0, len(arr)-1, len(arr)-1))