# Data structure and algorithms
# Insertion Sort
import random

def insertion_sort(arr: list) -> None:
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i-1

        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def main():
    arr = [random.randint(0,95) for _ in range(random.randint(5, 27))]
    print('Unsorted list of integers: ', arr)
    insertion_sort(arr)
    print('Sorted list of integers: ', arr)


if __name__ == "__main__":
    main()