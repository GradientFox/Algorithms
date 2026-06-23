def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        y = i
        while y > 0 and arr[y-1] > temp:
            arr[y] = arr[y-1]
            y -= 1
        arr[y] = temp

# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(my_list)
print("Отсортированный список:", my_list)