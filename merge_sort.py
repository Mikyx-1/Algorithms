# Merge sort implementation


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    
    left_part = arr[:mid]
    right_part = arr[mid:]

    left_part = merge_sort(left_part)
    right_part = merge_sort(right_part)

    merged = merge(left_part, right_part)

    return merged


def merge(left_part, right_part):
    new_arr = []
    i = j = 0
    while i < len(left_part) and j < len(right_part):
        if left_part[i] < right_part[j]:
            new_arr.append(left_part[i])
            i+= 1
        else:
            new_arr.append(right_part[j])
            j += 1

    while i < len(left_part):
        new_arr.append(left_part[i])
        i+=1

    while j < len(right_part):
        new_arr.append(right_part[j])
        j += 1

    return new_arr

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7, -3]
    print(merge_sort(arr))
