


def getRowSeparator(lengths, left, middle, right, horizontal, string=""):
    for i in range(len(lengths)+1):
        if i == 0:
            string += left + _repeat(horizontal, lengths[i] + 2)
        elif i < len(lengths):
            string += middle + _repeat(horizontal, lengths[i] + 2)
        else:
            string += right + "\n"
    return string

def getRowPopulated(lengths, data, left, middle, right, string=""):
    for i in range(len(lengths)+1):
        if i >= len(lengths):
            string += right + "\n"
        else:
            space = ((lengths[i]+2)-len(str(data[i])))
            spaceL = int(space/2)
            spaceR = spaceL + (0 if space%2 == 0 else 1)
            if i == 0:
                string += left + _repeat(" ", spaceL) + str(data[i]) + _repeat(" ", spaceR)
            else:
                string += middle + _repeat(" ", spaceL) + str(data[i]) + _repeat(" ", spaceR)
    return string
                

def _repeat(char, n):
    return (n * char) 


def prettiertable(n_cols, cols_names, data, type="default"):
    list_chars = []
    # MAPA DAS DIVISOS DA TABLE NA SAIDA:
    #
    # [0]   [10]  [1]   [10]  [2]
    # [9] Header 1 [9] Header 2 [9]
    # [3]   [10]  [4]   [10]  [5]
    # [9] Value 1  [9] Value 2  [9]
    # [3]   [10]  [4]   [10]  [5]
    # [9] Value 1a [9] Value 2a [9]
    # [6]   [10]  [7]   [10]  [8]

    # DEFINE OS CARACTERES A SEEM USADOS

    if type == "default":
        list_chars = ["\u2554","\u2566","\u2557","\u2560","\u256C","\u2563","\u255A","\u2569","\u255D","\u2551","\u2550"]
    elif type == "simple":
        list_chars = ["\u250C","\u252C","\u2510","\u251C","\u253C","\u2524","\u2514","\u2534","\u2518","\u2502","\u2500"]
    else:
        list_chars = ["+","+","+","+","+","+","+","+","+","|","-"]

    # INICIA A MONTAGEM DA TABELA:

    # CALCULA TAMANHO DAS COLUNAS
    col_len = []
    for i in range(n_cols):
        col_len.append(0) # zera a lista de tamanhos
    
    for item in data: # item = tuple na variavel data
        for col in range(n_cols): #col = elem dentro da tuple
            if len(str(item[col])) > col_len[col]:
                col_len[col] = len(str(item[col]))

    for item in range(len(cols_names)):
        if len(cols_names[item]) > col_len[item]:
            col_len[item] = len(cols_names[item])
    

    # INICIANDO PLOTAGEM DA TABELA

    # INICIA A STRING VAZIA
    str_table = ""

    # INICIA O TOPO
    str_table += getRowSeparator(col_len, list_chars[0], list_chars[1], list_chars[2], list_chars[10])

    # ADICIONANDO O TITULO
    str_table += getRowPopulated(col_len, cols_names, list_chars[9], list_chars[9], list_chars[9])

    # FINALIZANDO O TOPO
    str_table += getRowSeparator(col_len, list_chars[3], list_chars[4], list_chars[5], list_chars[10])

    # ADICIONANDO OS DEMAIS DADOS
    for i in range(len(data)):
        str_table += getRowPopulated(col_len, data[i], list_chars[9], list_chars[9], list_chars[9])

    # FECHANDO A TABELA
    str_table += getRowSeparator(col_len, list_chars[6], list_chars[7], list_chars[8], list_chars[10])
    return str_table










