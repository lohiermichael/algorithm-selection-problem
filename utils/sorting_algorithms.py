from typing import List
import random

"""
=====================
MERGE SORT
=====================
"""


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


"""
=====================
QUICK SORT
=====================
"""


def partition(L: List, left: int, right: int):
    """
        Makes a partition of the input list relatively to its first element
        Parameters
        ----------
        L (list): input list
        left (int): left index of the list to partition
        right (int): right index of the list to partition
        randomized (bool): if true the pivot is randomly chosen

        Returns
        -------
        Modifies the input list and returns the index of the position of the pivot
        """
    # Definition of the pivot
    rand_index = random.randint(left, right)
    pivot = L[rand_index]
    # Swap the rand element with the left element
    L[rand_index], L[left] = L[left], L[rand_index]
    # i is the index of the split between elements smaller and bigger than the pivot
    # j is the element that goes through the list
    i = left + 1
    for j in range(left + 1, right + 1):
        if L[j] < pivot:
            L[i], L[j] = L[j], L[i]
            i += 1
    # Final swap to  put the pivot at its right place
    L[left], L[i - 1] = L[i - 1], L[left]
    return i - 1


def quick_sort(L: List) -> list:
    """
    This function sorts the input list with in-place implementation, i.e.
    it keeps memory complexity quite low as contrary to the quick_sort_michael function
    no additional L_left and L_right are created.
    randomized (bool): if true the pivot is randomly chosen

    Parameters
    ----------
    L (list): input list

    Returns
    -------
    Sorted list
    """

    def sub_function_random(L: List, left: int, right: int):
        if left < right:
            i_pivot = partition(L, left=left, right=right)
            sub_function_random(L, left=left, right=i_pivot - 1)
            sub_function_random(L, left=i_pivot + 1, right=right)

    sub_function_random(L, left=0, right=len(L) - 1)
    return L
