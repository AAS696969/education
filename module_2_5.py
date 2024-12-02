def get_matrix(n, m, value):
    matrix = []
    for x in range(n):                 # внешний цикл для строк матрицы
        matrix.append([])              # добавляем пустую строку
        for y in range(m):             # внутренний цикл для столбцов матрицы
            matrix[x].append(value)    # заполняем список значениями value.
    print(matrix)
    return matrix
#matrix = get_matrix(n, m, value)
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)