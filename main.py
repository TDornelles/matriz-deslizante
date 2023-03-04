class Node:
    def __init__(self, moves):
        self.children = []
        self.moves = moves

# inserção de dados
print("Insira a matriz inicial e desejada:")
matrix = []
counter = 0
while counter < 6:
    try:
        line = input()
        contents = [line[0], line[2], line[4]]
        matrix.append(contents)
        counter = counter + 1
    except EOFError:
        break

matrizInicial = [matrix[0], matrix[1], matrix[2]]
matrizFinal = [matrix[3], matrix[4], matrix[5]]


# matrizInicial = [["a", "b", "e"], ["r", "g", "e"], ["e", "c", "c"]]
# matrizFinal = [["a", "b", "e"], ["e", "r", "g"], ["c", "c", "e"]]


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
    pilha = [Node([])]
    testado = []
    i = 0
    
    while len(pilha) > 0:
        no:Node = pilha.pop(0)
        repetido = False
        for j in testado:
            if j.count(1) == no.moves.count(1) and j.count(2) == no.moves.count(2) and j.count(3) == no.moves.count(3):
                repetido = True
        if (testado.count(no.moves) == 0 and repetido == False):
            i+=1
            testado.append(no.moves)
            # testar movimento
            mAux = matrizInicial.copy()
            change_state(no.moves, mAux)
            if mAux == matrizFinal:
                solved = True
                moves = no.moves
                break
            # criar filhos
            for n in range(3):
                childMoves = no.moves.copy()
                childMoves.append(n+1)
                # adicionar na pilha apenas se o mvoes nao tiver mais de 2 vezes o mesmo movimento
                if childMoves.count(n+1)<3:
                    newNode = Node(childMoves)
                    newNode.moves = childMoves
                    pilha.append(newNode)

    if solved:
        print("R1: "+str(moves.count(1))+", R2: "+str(moves.count(2))+", R3: "+str(moves.count(3)))
    else:
        print("impossible")

    print(i)
    

busca()
