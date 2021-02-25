import copy

def count_swap(arr, sorted_arr, mapping):
    swap_count = 0
    for idx in range(0, len(arr)):
        if arr[idx] == sorted_arr[idx]:
            continue
        else:
            arr[idx], arr[mapping[sorted_arr[idx]]] = arr[mapping[sorted_arr[idx]]], arr[idx]
            mapping[arr[mapping[sorted_arr[idx]]]] = mapping[sorted_arr[idx]]
            mapping[arr[idx]] = idx
            swap_count += 1

    return swap_count

def lilysHomework(arr):
    arr_len = len(arr)
    sorted_arr = sorted(arr)

    mapping = {}
    for idx in range(0, arr_len):
        mapping[arr[idx]] = idx

    asc_swap_count = count_swap(copy.copy(arr), sorted_arr, copy.copy(mapping))
    desc_swap_count = count_swap(copy.copy(arr), sorted_arr[::-1], copy.copy(mapping))

    return min(asc_swap_count, desc_swap_count)
