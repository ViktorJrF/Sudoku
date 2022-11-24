#Sudoku incorrecto
# sudoku = [
#     [1,2,3,4,5,6,7,8,9],
#     [2,3,4,5,6,7,8,9,1],
#     [3,4,5,6,7,8,9,1,2],
#     [5,2,3,4,5,6,7,8,9],
#     [6,2,3,4,5,6,6,7,8],
#     [7,2,3,4,5,6,7,8,9],
#     [8,2,3,4,5,6,7,8,8],
#     [9,2,2,3,4,5,5,6,7],
#     [4,2,3,4,5,3,4,5,6],
# ]

#sudoku correcto
sudoku = [
    [4,1,3,8,2,5,6,7,9],
    [5,6,7,1,4,9,8,3,2],
    [2,8,9,7,3,6,1,4,5],
    [1,9,5,4,6,2,7,8,3],
    [7,2,6,9,8,3,5,1,4],
    [3,4,8,5,1,7,2,9,6],
    [8,5,1,6,9,4,3,2,7],
    [9,7,2,3,5,8,4,6,1],
    [6,3,4,2,7,1,9,5,8],
]

for i in range(9):

    setFila = set(sudoku[i])
    arrcol = []
    cuadrante = []
    
    for j in range(9):
        arrcol.append(sudoku[j][i])
        setCol = set(arrcol)
 
    for filac in range(3):
        filacuadrante = ((i % 3)* 3) + filac
        for columnac in range(3):
            if (i<3):
                cuadrante.append(sudoku[filacuadrante][columnac])
            elif (i>2 & i<6):
                cuadrante.append(sudoku[filacuadrante][columnac + 3])
            else:
                cuadrante.append(sudoku[filacuadrante][columnac + 6])
    setCuadrante = set(cuadrante)

    if (len(sudoku[i]) != len(setFila)):
        print("Número duplicado en fila:","\n", sudoku[i])
        break
    
    if (len(arrcol) != len(setCol)):
        print("Número duplicado en columna:","\n", arrcol)
        break
    
    if (len(cuadrante) != len(setCuadrante)):
        print("Número duplicado en cuadrante:\n", cuadrante[0:3],"\n",cuadrante[3:6],"\n",cuadrante[6:9])
        break
    

if (i == 8):
    print("Sudoku resuelto correctamente")
else:
    print("Sudoku no resuelto")