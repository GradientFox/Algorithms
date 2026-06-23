def selection_sort(arr):
    for i in range(len(arr)):
        min_ind = i
        for y in range(i+1, len(arr)):
            if arr[y] <= arr[min_ind]:
                min_ind = y
        arr[i], arr[min_ind] = arr[min_ind], arr[i]


# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(my_list)
print("Отсортированный список:", my_list)