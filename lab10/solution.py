import numpy as np

def make_table(rows,columns):
    a = np.arange(rows*columns).reshape(rows,columns)
    a = a + 1
    return a.tolist()

def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    a = np.array(matrix)
    return a[row_start:row_stop+1 , column_start:column_stop+1].tolist()

def replace_rectangle(matrix,row_start,row_stop,column_start,column_stop, value):
    a = np.array(matrix)
    a[row_start:row_stop+1 , column_start:column_stop+1] = value
    return a.tolist()

def matrix_vector_product(matrix,vector):
    a = np.array(matrix)
    b = np.array(vector)
    return (a @ b).tolist()

def matrix_multiply(left,right):
    a = np.array(left)
    b = np.array(right)
    return (a @ b).tolist()

def transpose_matrix(matrix):
    a = np.array(matrix)
    return a.T.tolist()

def solve_system(matrix,vector):
    a = np.array(matrix)
    b = np.array(vector)
    return np.linalg.solve(a,b).tolist()



mat = make_table(3,4)
mat1 = make_table(4,3)
print(rectangle(mat, 1, 2, 0, 1))
print(mat)
print(replace_rectangle(mat,1,2,0,1,99))
print(matrix_vector_product(mat,[0,1,2,3]))
print(mat, mat1)
print(transpose_matrix(mat))

