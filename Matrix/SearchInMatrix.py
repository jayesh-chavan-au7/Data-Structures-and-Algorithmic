global row,column
row = int(input('enter no of rows : '))
column = int(input('enter no of columns : '))

matrix = [[int(input('enter element of {}th row and {}th coloumn : '.format(i,j))) for j in range(column)] for i in range(row)]

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j],end=" ")
        print()

printMatrix(matrix)

def search(matrix,element):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                print('element at {}th row and {}th coloumn'.format(i,j))
                count += 1
    if count > 0 :
        print('elment ocurred in matrix is {} times in matrix'.format(count))
        return
    else: print('element not found')

while True:
    try:
        element = int(input('enter an element to search : '))
        search(matrix,element)
    except:
        exit()