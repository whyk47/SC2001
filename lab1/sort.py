import random
from collections.abc import MutableSequence


def merge_sort(arr: MutableSequence, start: int, end: int) -> int:
    cmp = 0
    if start < end:
        mid = (start + end) // 2
        cmp += merge_sort(arr, start, mid)
        cmp += merge_sort(arr, mid + 1, end)
        cmp += merge(arr, start, end)
    return cmp


def merge(arr: MutableSequence, start: int, end: int) -> int:
    if start >= end:
        return 0
    mid = (start + end) // 2
    temp = []
    cmp = 0
    i, j = start, mid + 1
    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
        cmp += 1
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= end:
        temp.append(arr[j])
        j += 1
    for i in range(len(temp)):
        arr[start + i] = temp[i]
    return cmp


def insertion_sort(arr: MutableSequence, start: int, end: int) -> int:
    if start >= end:
        return 0
    cmp = 0
    for i in range(start + 1, end + 1):
        key = arr[i]
        j = i - 1
        while j >= start and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            cmp += 1
        if j >= start:
            cmp += 1  # For the last comparison when while condition fails
        arr[j + 1] = key
    return cmp


def hybrid_sort(arr: MutableSequence, start: int, end: int, threshold: int = 3) -> int:
    cmp = 0
    if end - start + 1 <= threshold:
        cmp += insertion_sort(arr, start, end)
    else:
        mid = (start + end) // 2
        cmp += hybrid_sort(arr, start, mid, threshold)
        cmp += hybrid_sort(arr, mid + 1, end, threshold)
        cmp += merge(arr, start, end)
    return cmp
