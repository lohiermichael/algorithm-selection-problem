from typing import List


def merge_sort(L: List) -> List:
    """
    This will perform the merge sort algorithm.
    This is a compact version of the previous algorithm.
    It will save some space memory
    Args:
        L(list): Input list
    Returns:
        Sorted list
    """
    if len(L) <= 1:
        return L
    else:
        mid = len(L) // 2
        L_left = merge_sort(L[:mid])
        L_right = merge_sort(L[mid:])
        i, j, k = 0, 0, 0
        while i < len(L_left) and j < len(L_right):
            if L_left[i] < L_right[j]:
                L[k] = L_left[i]
                i += 1
            else:
                L[k] = L_right[j]
                j += 1
            k += 1
        while i < len(L_left):
            L[k] = L_left[i]
            i += 1
            k += 1

        while j < len(L_right):
            L[k] = L_right[j]
            j += 1
            k += 1
        return L
