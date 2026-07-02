def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for y in range(i):
            if arr[y] > arr[y+1]:
                arr[y], arr[y+1] = arr[y+1], arr[y]


# Пример использования
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Отсортированный список:", my_list)
