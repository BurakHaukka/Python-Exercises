a = [5, 4, 3, -1, 9, 6]


def bubble_sort(a):
    n = len(a)
    swapped = False # There is no swapping so swapped is false
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                swapped = True #swapping happens here, as long as happens it is = True
                a[j], a[j + 1] = a[j + 1], a[j]
        if not swapped: # if no swapping needed then exits
            break
    return a


print("result:", bubble_sort(a))
