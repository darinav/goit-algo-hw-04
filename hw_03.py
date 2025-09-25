import timeit
import random
import argparse

def generate_numbers(length: int, range_min: int = 1, range_max: int = 1_000_000) -> list:
    return [random.randint(range_min, range_max) for _ in range(length)]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def main():
    parser = argparse.ArgumentParser(description="Comparing sorting algorithms")
    parser.add_argument('size', type=int, help='Elements amount to sort')
    args = parser.parse_args()

    print(f"--- Testing Sort Algorithms on {args.size} Random Elements ---")
    data = generate_numbers(args.size)

    setup_code = "from __main__ import merge_sort, insertion_sort"

    stmt_merge = "merge_sort(data.copy())"
    stmt_insertion = "insertion_sort(data.copy())"
    stmt_timsort = "sorted(data.copy())"

    runs = 1 if args.size > 10000 else 10

    t_merge = timeit.timeit(stmt=stmt_merge, setup=setup_code, globals={'data': data}, number=runs)
    print(f"Merge Sort: {t_merge/runs:.6f} seconds")

    t_insertion = timeit.timeit(stmt=stmt_insertion, setup=setup_code, globals={'data': data}, number=runs)
    print(f"Insertion Sort: {t_insertion/runs:.6f} seconds")

    t_timsort = timeit.timeit(stmt=stmt_timsort, setup=setup_code, globals={'data': data}, number=runs)
    print(f"Timsort (built-in): {t_timsort/runs:.6f} seconds")

if __name__ == "__main__":
    main()