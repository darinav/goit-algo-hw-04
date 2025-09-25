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

"""
    *** Результати ***

--- Testing Sort Algorithms on 100 Random Elements ---
Merge Sort: 0.000077 seconds
Insertion Sort: 0.000107 seconds
Timsort (built-in): 0.000003 seconds

--- Testing Sort Algorithms on 1000 Random Elements ---
Merge Sort: 0.001000 seconds
Insertion Sort: 0.009950 seconds
Timsort (built-in): 0.000028 seconds

--- Testing Sort Algorithms on 10000 Random Elements ---
Merge Sort: 0.010080 seconds
Insertion Sort: 1.046503 seconds
Timsort (built-in): 0.000527 seconds

--- Testing Sort Algorithms on 20000 Random Elements ---
Merge Sort: 0.025240 seconds
Insertion Sort: 4.565582 seconds
Timsort (built-in): 0.001427 seconds

--- Testing Sort Algorithms on 50000 Random Elements ---
Merge Sort: 0.056660 seconds
Insertion Sort: 27.807289 seconds
Timsort (built-in): 0.003801 seconds

*** Висновки ***
В ході емпіричного дослідження ми порівняли продуктивність трьох 
алгоритмів сортування Insertion Sort, Merge Sort та вбудованого Timsort
на наборах даних різного розміру, від 100 до 50,000 елементів. 
Результати наочно демонструють теоретичні оцінки складності алгоритмів.

Сортування вставками (Insertion Sort) показало квадратичну складність O(n²). 
Це підтверджується даними: при збільшенні масиву з 10,000 до 20,000 
елементів час виконання зріс у чотири рази, з ~1 до ~4.5 секунд, 
що робить його неефективним для великих обсягів даних.

Натомість сортування злиттям (Merge Sort) продемонструвало лог-лінійну 
складність O(n log n). Зростання часу було набагато більш контрольованим і передбачуваним, 
що робить його надійним вибором для великих, хаотично перемішаних масивів.

Найефективнішим виявився вбудований алгоритм Timsort. 
Наші дані показують, що він значно випереджає інші алгоритми на всіх наборах даних. 
Його ефективність пояснюється гібридною природою: він використовує сильні сторони обох підходів. 
Timsort розбиває масив на невеликі, частково впорядковані частини ("runs") і швидко 
сортує їх за допомогою Insertion Sort, який є дуже ефективним на малих та майже 
відсортованих даних. Потім він ефективно зливає ці частини, використовуючи принципи Merge Sort.

Таким чином, Timsort є значно продуктивнішим не лише тому, що він вбудований, 
а й тому, що його гібридна стратегія оптимально адаптується до характеристик реальних, 
часто частково впорядкованих даних. Саме ця інтелектуальна оптимізація робить 
його стандартним вибором у Python.
"""