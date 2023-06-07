def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
numbers = [5, 3, 4, 2, 1, 100, 23, 18, 33]
bubble_sort(numbers)
print("Sorted numbers:\t", numbers)
