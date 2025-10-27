# lst = [3,5,2,6,4,9,8,1]

# while True:
#     if len(lst)>1:
#         mid =len(lst)//2
#         l=lst[:mid]
#         r=lst[mid:]
#         print(l,r)
#     if len(l) >1  or len(r) >1:
#         mid = len(l)//2
#         l=l[:mid]
#         r=r[:mid]
#         print(l,r)
#         break
#
#
#
# def merge_sort(arr, l, r):
#     if l < r:
#         mid = (l + r) // 2  # Find the middle index
#
#         # Sort the left half
#         merge_sort(arr, l, mid)
#
#         # Sort the right half
#         merge_sort(arr, mid + 1, r)
#
#         # Merge both halves
#         merge(arr, l, mid, r)
#
#
# def merge(arr, l, mid, r):
#     # Create temp arrays
#     left = arr[l:mid + 1]
#     right = arr[mid + 1:r + 1]
#
#     i = j = 0
#     k = l
#
#     # Merge until one list is finished
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             arr[k] = left[i]
#             i += 1
#         else:
#             arr[k] = right[j]
#             j += 1
#         k += 1
#
#     # Copy remaining elements (if any)
#     while i < len(left):
#         arr[k] = left[i]
#         i += 1
#         k += 1
#
#     while j < len(right):
#         arr[k] = right[j]
#         j += 1
#         k += 1
#
#
# # Example
# arr = [7, 3, 8, 2, 5, 1, 4, 6]
# merge_sort(arr, 0, len(arr) - 1)
# print("Sorted array:", arr)
def merge_sort(arr):
    print(f"Splitting: {arr}")

    if len(arr) <= 1:
        return arr


    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])


    sorted_arr = merge(left_half, right_half)
    print(f"Merging: {left_half} and {right_half} → {sorted_arr}")
    return sorted_arr


def merge(left, right):
    result = []
    i = j = 0

    # Compare elements and merge them
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Example
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original Array:", arr)

sorted_arr = merge_sort(arr)
print("\nFinal Sorted Array:", sorted_arr)
