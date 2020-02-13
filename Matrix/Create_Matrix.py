global row,col
row = int(input('Enter no of rows : '))
col = int(input('Enter no of col : '))

def matrix_using_loop(row,col):
    matrix = []
    for i in range(row):
        a = []
        for j in range(col):
            a.append(int(input('Enter element of {0} row and {1} col : '.format(i,j))))
        matrix.append(a)
    return print_matrix(matrix)

def matrix_using_list_comprehension(row,col):
    matrix = [ [ int(input('Enter element of {0} row and {1} col : '.format(i,j))) for j in range(col) ] for i in range(row)]
    return print_matrix(matrix)

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j],end=" ")
        print()

choice = int(input('Enter 1 for loop method and 2 for list comprehension method: '))

if choice == 1:
    matrix_using_loop(row,col)
elif choice == 2:
    matrix_using_list_comprehension(row,col)