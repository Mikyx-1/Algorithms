# Implementation of quicksort following animation on https://www.youtube.com/watch?v=WprjBK0p6rw


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
                cache = arr[ptr1]
                arr[ptr1] = arr[ptr2]
                arr[ptr2] = cache
                if i == len(arr) - 1:
                    index = ptr2
            elif ptr1 == ptr2:
                pass
        ptr1 += 1
    return arr, index


def quicksort(arr, start, end):
    if  end > start:
        sorted_arr, new_pivot_index = sort_with_pivot(arr, start, end)
        left_sorted_arr = quicksort(arr, start, new_pivot_index-1)
        right_sorted_arr = quicksort(arr, new_pivot_index+1, end)

def sort(arr):
    quicksort(arr, 0, len(arr)-1)
    return arr


arr = [3, 2, 0, 1, 5, 8, 7, 6, 9, 4]
print(sort(arr))