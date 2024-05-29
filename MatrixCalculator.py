#Caleb Scott
import random
import multiprocessing as mp

print("Enter 0 if you would like to multiply two random matrices.")
matrixOneCount = int(input("Enter the number of columns for the first matrix: "))
matrix1 = []
matrix2 = []

def worker_task(row, matrix2, result, row_idx):
    matrix2Cols = len(matrix2[0])
    matrix2Rows = len(matrix2)
    for col in range(matrix2Cols):
        sum = 0
        for item in range(matrix2Rows):
            sum += matrix1[row_idx][item] * matrix2[item][col]
        result[row_idx][col] = sum


def calculate():
    matrix1Rows = len(matrix1)
    matrix2Rows = len(matrix2)

    matrix1Cols = len(matrix1[0])
    matrix2Cols = len(matrix2[0])
    
    if matrix1Cols != matrix2Rows:
        print("cannot compute! -> matrix one columns are not equal to matrix two rows")
        print("Matrix one rows:", matrix1Rows, "Matrix two columns:", matrix2Cols)
        
    else:
        result = mp.Manager().list([[0 for y in range(matrix2Cols)] for y in range(matrix1Rows)])
        processes = []
        
        for row in range(matrix1Rows):
            p = mp.Process(target=worker_task, args=(row, matrix2, result, row))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        print("Result:", list(result))
        for row in result:
            print(row)

#random calculation
if matrixOneCount == 0:
    rows1 = random.randint(3, 12)
    cols1 = random.randint(3, 12)
    rows2 = cols1
    cols2 = random.randint(3, 12)

    matrix1 = [[random.randint(0, 9) for j in range(cols1)] for j in range(rows1)]
    matrix2 = [[random.randint(0, 9) for l in range(cols2)] for l in range(rows2)]

    print("Matrix one:")
    for row in matrix1:
        print(row)

    print("Matrix two:")
    for row in matrix2:
        print(row)

    calculate()
    
#user's calculation            
if matrixOneCount != 0:
    for i in range(matrixOneCount):
        row = []
        print("Enter row for column ", i)
        element = int(input("--> "))
        row = [int(x) for x in str(element)]
        matrix1.append(row)

    matrixTwoCount = int(input("Enter the number of columns for the second matrix: "))

    for j in range(matrixTwoCount):
        row = []
        print("Enter row for column ", j)
        element = int(input("--> "))
        row = [int(x) for x in str(element)]
        matrix2.append(row)
    
    print("First matrix:", matrix1)
    print("Second matrix:", matrix2)

    calculate()


