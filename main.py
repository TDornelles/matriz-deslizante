import numpy as np

#ableu = "a b e\ne r g\ne c c\ne a b\ne r g\ne c c"

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

start_matrix = [matrix[0], matrix[1], matrix[2]]
end_matrix = [matrix[3], matrix[4], matrix[5]]

#array = np.array(start_matrix)
#
# print(array)
# #print(end_matrix)

matriz = [["a", "b", "c"], ["e", "f", "g"], ["a", "c", "c"]]
changes = []
print(matriz)



def slide(line):
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


def change_state(rotations):
    for i in rotations:
        slide(i)



buffer_matrix = start_matrix


slide(1)
print(matriz)
print(changes)
