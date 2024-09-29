def print_matrix(mat, name = None, val_len=3):
    out_str = ""
    if name is not None:
        out_str += ("--" + "-" * val_len + "-") * len(mat[0]) + "-\n"
        out_str += str(name) + ":\n"

    # draw a starting line
    out_str += ("--" + "-" * val_len + "-") * len(mat[0]) + "-\n"

    # add all the values
    for row in mat:
        for val in row:
            val = str(val)
            out_str += "| " + " " * (val_len - len(val)) + val + " "
        out_str += "|\n"

        if row is not mat[-1]:
            # Draw the lines between rows
            out_str += ("|-" + "-" * val_len + "-") * len(mat[0]) + "|\n"
    # Draw the last line
    out_str += ("--" + "-" * val_len + "-") * len(mat[0]) + "-\n"
    print(out_str)

def get_next_conv(img, kernel=None):
    if kernel is None:
        kernel=[[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
    conv = []
    for s_row in range(len(img) - len(kernel) + 1):
        for s_column in range(len(img[0]) - len(kernel[0]) + 1):
            conv = [[img[s_row][s_column], img[s_row][s_column+1], img[s_row][s_column+2]],
                    [img[s_row+1][s_column], img[s_row+1][s_column+1], img[s_row+1][s_column+2]],
                    [img[s_row+2][s_column], img[s_row+2][s_column+1], img[s_row+2][s_column+2]]]
            yield conv


img = [[237, 90, 40, 207, 112],
    [191, 123, 158, 55, 128],
    [36, 168, 149, 225, 176],
    [10, 113, 128, 244, 58],
    [66, 87, 225, 59, 236]]

kernel = [
    [-1,-1,-1],
    [-1,8,-1],
    [-1,-1,-1]
]

def fun_convolusion(img, kernel):
    count = 0
    nivel = 1
    num_lista = 0
    lista = [[],[],[],[],[],[],[],[],[]]
    for k in range(0,10):
        contador = 0
        # print(f"nivel {nivel}")
        # print(lista)
        if nivel == 1:
            fila = -1
            columna = -1
        elif nivel == 2:
            fila = -2
            columna = -1
        elif nivel == 3:
            fila = -3
            columna = -1
        elif nivel == 4:
            count = 0
            fila = 0
            columna = -1
        elif nivel == 5:
            count = 1
            fila = -1
            columna = -1
        elif nivel == 6:
            count = 2
            fila = -2
            columna = -1
        elif nivel == 7:
            count = 0
            fila = 1
            columna = -1
        elif nivel == 8:
            count = 1
            fila = 0
            columna = -1
        elif nivel == 9:
            count = 2
            fila = -1
            columna = -1
        count += 1
        num_lista += 1
        nivel += 1
        for i in kernel:
            for j in i:
                try:
                    if contador < 3:
                        lista[num_lista-1].append(j*(img[fila+(count)][columna+(count)]))
                        columna += 1
                        contador += 1
                    elif contador == 3:
                        contador = 0
                        columna = -1
                        fila += 1
                        lista[num_lista-1].append(j*(img[fila+(count)][columna+(count)]))
                        columna += 1
                        contador += 1
                except:
                    pass
    convolusion = [[],
                   [],
                   []]
    numero = 0
    inicio = 0
    final = 3
    for j in range(0,3):
        for i in lista[inicio:final]:
            suma = sum(i)
            if suma >= 255:
                suma = 255
            elif suma <= 0:
                suma = 0
            convolusion[numero].append(suma)
        inicio += 3
        final += 3
        numero += 1
    return convolusion
print_matrix(fun_convolusion(img, kernel))

# print_matrix(kernel, "Kernel", val_len=2)
# print_matrix(img, "Imagen Original")


# print(get_next_conv(img))
# for conv in get_next_conv(img):
#     print_matrix(conv)

# convolution = [[255, 255, 0],
#                [255, 115, 0],
#                [255, 0, 0]]

# convolutions = get_next_conv(img, kernel)
# next_conv = next(convolutions)
# print_matrix(next_conv)