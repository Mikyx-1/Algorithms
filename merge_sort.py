# Merge sort algorithm
# BigO nlog(n)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    
    left_part = arr[:mid]
    right_part = arr[mid:]

    left_part = merge_sort(left_part)
    right_part = merge_sort(right_part)

    merged = []
    i = j = 0
    while i < len(left_part) and j < len(right_part):
        if left_part[i] < right_part[j]:
            merged.append(left_part[i])
            i+=1
        else:
            merged.append(right_part[j])
            j += 1

    while i < len(left_part):
        merged.append(left_part[i])
        i+= 1
    while j < len(right_part):
        merged.append(right_part[j])
        j += 1

    return merged

if __name__ == "__main__":
    print(merge_sort([12, 11, 13, 5, 6, 7, -3]))
