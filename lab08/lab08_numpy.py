import numpy as np

print("Задание 1. Создание массивов")
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3, dtype=int)

print("hours:", hours)
print("shape:", hours.shape, "ndim:", hours.ndim,
      "size:", hours.size, "dtype:", hours.dtype)

print("\nЗадание 2. Срезы вектора")
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Индексы 2–5:", hours[2:6])
print("Каждый второй:", hours[::2])
print("В обратном порядке:", hours[::-1])

print("\nЗадание 3. Строки и столбцы")
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
print("shape:", temperatures.shape, "ndim:", temperatures.ndim,
      "size:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])
center = temperatures[:2, 1:3]
print("Центральный фрагмент:\n", center)
print("shape:", center.shape)

print("\nЗадание 4. Прямоугольные срезы")
matrix = np.arange(1, 26).reshape(5, 5)

first_rows = matrix[:3, :]
print("Первые три строки:\n", first_rows)
print("shape:", first_rows.shape)

last_rows = matrix[-2:, :]
print("Последние две строки:\n", last_rows)
print("shape:", last_rows.shape)

first_columns = matrix[:, :2]
print("Первые два столбца:\n", first_columns)
print("shape:", first_columns.shape)

fragment = matrix[1:4, 2:5]
print("Строки 1–3, столбцы 2–4:\n", fragment)
print("shape:", fragment.shape)

corner = matrix[-2:, -2:]
print("Правый нижний угол:\n", corner)
print("shape:", corner.shape)

print("\nЗадание 5. Изменение срезов")
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print("Пример с вектором:", vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print("Пример с матрицей:\n", small_matrix)


changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1
print("Изменённый hours:", changed_hours)
print("Исходный hours:", hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100
print("Изменённая матрица:\n", changed_matrix)
print("Исходная матрица:\n", matrix)

print("\nЗадание 6. Изменение формы")
numbers = np.arange(12)

table = numbers.reshape(3, 4)
transposed = table.T
print("numbers.shape:", numbers.shape)
print("table.shape:", table.shape)
print("transposed.shape:", transposed.shape)
