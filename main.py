import numpy as np


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.moves = []




# print("Insira a matriz inicial e desejada:")
# matrix = []
# counter = 0
# while counter < 6:
#     try:
#         line = input()
#         contents = [line[0], line[2], line[4]]
#         matrix.append(contents)
#         counter = counter + 1
#     except EOFError:
#         break

# matrizInicial = [matrix[0], matrix[1], matrix[2]]
# matrizFinal = [matrix[3], matrix[4], matrix[5]]



matrizInicial = [["a", "b", "e"], ["r", "g", "e"], ["e", "c", "c"]]
matrizFinal = [["a", "b", "e"], ["e", "r", "g"], ["c", "c", "e"]]



def slide(line, matriz):
    match line:
        case 1:
            buffer = [matriz[0][2], matriz[0][0], matriz[0][1]]
            matriz[0] = buffer
        case 2:
            buffer = [matriz[1][2], matriz[1][0], matriz[1][1]]
            matriz[1] = buffer
        case 3:
            buffer = [matriz[2][2], matriz[2][0], matriz[2][1]]
            matriz[2] = buffer


def change_state(rotations, matriz):
    for i in rotations:
        slide(i, matriz)



def busca():
    solved = False
    moves = []
    pilha = [Node(0)]
    testado = []
    i = 0
    
    while len(pilha) > 0:
        no:Node = pilha.pop(0)
        if (testado.count(no.moves) == 0 or no.value < 13):
            i+=1
            testado.append(no.moves)
            # testar movimento
            mAux = matrizInicial.copy()
            if no.value != 0: change_state(no.moves, mAux)
            if mAux == matrizFinal:
                solved = True
                moves = no.moves
                break
            for n in range(3):
                childMoves = no.moves.copy()
                childMoves.append(n+1)
                newNode = Node(n+1+no.value)
                newNode.moves = childMoves
                pilha.append(newNode)

    if solved:
        print(moves)
    else:
        print("impossible")




# def busca():
#     tries = 0
#     solved = False
#     moves = []
#     for i in mD:
#         tries = tries + 1
#         mAux = matrizInicial.copy()
#         change_state(mD[i], mAux)
#         if mAux == matrizFinal:
#             moves = mD[i]
#             solved = True
#             break

#     if solved == False:
#         print("impossivel")
#     else:
#         for i in moves:
#             print("R"+ str(moves[i-1]), end=" ")
        
#         print()
        
#     print(tries)
    

busca()
