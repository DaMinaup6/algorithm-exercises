def count_swap(arr, sorted_arr, mapping):
    swap_count = 0
    for idx in range(0, len(arr)):
        if arr[idx] == sorted_arr[idx]:
            continue
        else:
            sorted_idx = mapping[sorted_arr[idx]]
            arr[idx], arr[sorted_idx] = arr[sorted_idx], arr[idx]
            mapping[arr[sorted_idx]], mapping[arr[idx]] = sorted_idx, idx

            swap_count += 1

    return swap_count

def lilysHomework(arr):
    mapping = {}
    for idx in range(0, len(arr)):
        mapping[arr[idx]] = idx

    sorted_arr = sorted(arr)
    asc_swap_count  = count_swap(arr.copy(), sorted_arr,       mapping.copy())
    desc_swap_count = count_swap(arr.copy(), sorted_arr[::-1], mapping.copy())

    return min(asc_swap_count, desc_swap_count)
