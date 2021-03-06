# Data structure and algorithms
# Bubble Sort
import random

def bubble_sort(arr: list) -> None:
    l = len(arr)

    for i in range(l-1):
        for j in range(l-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def main():
    arr = [random.randint(0,95) for _ in range(random.randint(5, 27))]
    print('Unsorted list of integers: ', arr)
    bubble_sort(arr)
    print('Sorted list of integers: ', arr)


if __name__ == "__main__":
    main()