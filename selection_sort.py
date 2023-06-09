"""
selection sort(сортировка выбором) - проходим по массиву в поисках
максимального элемента. Найденный максимум меняем местами с
последним элементом. Неотсортированная часть массива
уменьшилась на один элемент
(не включает последний элемент, куда мы переставили найденный максимум).
К этой неотсортированной части применяем те же действия — находим максимум
и ставим его на последнее место в неотсортированной части массива.И так
продолжаем до тех пор, пока неотсортированная часть массива не уменьшится до
одного элемента.
"""


def findSmallest(arr):
    """ Ищет наименьший элемент массива. """
    smallest = arr[0]  # Хранит наименьший элемент
    smallest_index = 0  # Хранит индекс наименьшего значения
    for i in range(1, len(arr)):  # Начинается с 1, потому что мы используем первый элемент
        # массива arr[0] в качестве начального значения переменной smallest в функции findSmallest.
        if arr[i] < smallest:  # Сравнивает текущий элемент с наименьшим
            smallest = arr[i]  # Если текущий меньше наименьшего, то текущий становится наименьшим
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    """ Сортирует массив. """
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)  # Хранит индекс наименьшего значения, который получили из функции
        newArr.append(arr.pop(smallest))  # Удаляем наименьший элемент из массива по определенному индексу
        # и добавляем его в начало нового
    return newArr


print(selectionSort([5, 3, 6, 2, 10]))
