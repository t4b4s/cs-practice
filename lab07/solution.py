import numpy as np

def reshape_rows(values: list[float], width: int):
    a = np.asarray(values)
    rows = len(values) // width
    return a.reshape(rows, width).tolist()
    
def block(matrix: list[list[float]], rows: list[int], columns: list[int]):
    a = np.asarray(matrix)
    return a[np.ix_(rows,columns)].tolist()



print(reshape_rows([12, 14.5, 11, 13, 15.5, 10.5], 3))
# [[12.0, 14.5, 11.0], [13.0, 15.5, 10.5]]

print(block([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [0, 2], [1, 2]))
# [[2.0, 3.0], [8.0, 9.0]]

##column_means([[1, 2], [3, 4], [5, 6]])    # [3.0, 4.0]
##column_range([[1, 2], [5, 7]], 1)         # 5.0
