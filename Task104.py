def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivor = array[0]
    less = [i for i in array[1:] if i <= pivor]
    greater = [i for i in array[1:] if i > pivor]
    return quick_sort(less) + [pivor] + quick_sort(greater)


print(quick_sort([14, 5, 9, 6, 3, 8, 7, 5, 2, 7]))
