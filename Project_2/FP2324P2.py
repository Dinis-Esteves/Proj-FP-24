def cria_intersecao(column, row):
    """
    Create and intersection

    Args:
        column (str): The letter corresponding to the column
        row (int): the number corresponding to the row

    returns:
        intersection
    """
    if type(column) == str and type(row) == int and len(column) == 1 and (ord(column) - 64>=1) and (ord(column) - 64<=19)\
    and (row>=1) and (row<=19):
        return (column, row)
    raise ValueError("cria_intersecao: argumentos invalidos")

def obtem_col(inter):
    """
    Return the letter of the column of the intersection

    Args:
        intersection

    Returns:
        inter: the number of the row    
    """
    return inter[0]

def obtem_lin(inter):
    """
    Return the number of the row of the intersection

    Args:
        intersection

    Returns:
        inter: the letter of the column
    """
    return inter[1]

def eh_intersecao(inter):   
    """
    Check if the arguments is an intersection

    Args:
        Universal
        Universal

    Returns:
        bool: True if it is an intersection, False otherwise.
    """
    return type(inter) == tuple and len(inter) == 2 and type(obtem_col(inter)) == str\
    and len(obtem_col(inter)) == 1 and type(obtem_lin(inter)) == int and \
    (ord(obtem_col(inter)) - 64)>=1 and (ord(obtem_col(inter))) - 64<=19 and obtem_lin(inter) <= 19\
    and obtem_lin(inter) >= 1

def intersecoes_iguais(inter1, inter2):
    """
    Check if two intersections are equal.

    This function takes two intersections and returns True if they are equal
    (i.e., they have the same row and column), and False if they are not equal.

    Args:
        Universal
        Universal

    Returns:
        bool: True if the intersections are equal, False otherwise.
    """
    return obtem_lin(inter1) == obtem_lin(inter2) and obtem_col(inter1) == obtem_col(inter2)

def intersecao_para_str(inter):
    """
    Convert a intersection to a string

    Args:
        intersection

    Returns:
        string: for example 'A1'
            
    """
    return f'{obtem_col(inter)}{obtem_lin(inter)}'

def str_para_intersecao(cc):
    """
    Convert a string to a intersection

    Args:
        string: for example 'F3'

    Returns:
        intersection
    """
    return cria_intersecao(str(cc[0]), int(cc[1:]))

def lista_para_strings_intersecao(tup):
    """
    Convert a tuple of strings to intersctions

    Args:
        tuple: for example ('A1', 'F4')

    Returns:
        tuple: a tuple with intersections
    """
    tup_inter = ()
    for i in tup:
        tup_inter += (str_para_intersecao(i),)
    return tup_inter

def obtem_intersecoes_adjacentes(inter, inter_max):
    """
    Find the adjacent intersection

    Args:
        intersection: the intersection we want to check their closest ones
        intersection: the last intersection of the tuple

    Returns:
        tuple: a tuple with the adjacent intersections
    """
    inter_adj_cima = (obtem_col(inter), obtem_lin(inter) + 1)   
    inter_adj_baixo = (obtem_col(inter), obtem_lin(inter) - 1)
    inter_adj_esquerda = (chr(ord(obtem_col(inter))-1), obtem_lin(inter))
    inter_adj_direita = (chr(ord(obtem_col(inter))+1), obtem_lin(inter))
    inter_adj = ()
    for i in (inter_adj_baixo, inter_adj_esquerda, inter_adj_direita, inter_adj_cima):
        if eh_intersecao(i) and obtem_lin(i) <= obtem_lin(inter_max) and ord(obtem_col(i)) <= ord(obtem_col(inter_max)):
            inter_adj += (i,)
    return inter_adj

def ordena_intersecoes(tup_inter):
    """
    Sorts a list of intersections by the order of reading

    Args:
        tuple: a tuple with intersections

    Returns:
        tuple: a tuple with the same intersection but sorted by the order of reading
    """
    tup_inter_ordenado = ()
    n = 1
    while len(tup_inter) != len(tup_inter_ordenado):
        for i in sorted(tup_inter):
            if obtem_lin(i) == n:
                tup_inter_ordenado += (i,)
        n += 1
    return tup_inter_ordenado

def cria_pedra_branca():
    """ 	
    Creates a white stone

    Args:
        
    Returns:
        white stone
    """
    return 'O'

def cria_pedra_preta():
    """ 	
    Creates a black stone

    Args:
        
    Returns:
        black stone
    """
    return 'X'

def cria_pedra_neutra():
    """ 	
    Creates a neutral stone

    Args:

    Returns:
        "same de cima" stone
    """
    return '.'

def eh_pedra(pedra):
    """ 	
    Check if the argument is a stone

    Args:
        Universal

    Returns:
        boolean: True if the argument is a stone, False if it's not
    """
    return pedra in ('.', 'X', 'O')

def eh_pedra_branca(pedra):
    """ 	
    Check if the argument is a white stone

    Args:
        Universal 

    Returns:
        boolean: True if the argument is a white stone, False if it's not
    """
    return pedra == 'O'

def eh_pedra_preta(pedra):
    """ 	
    Check if the argument is a black stone

    Args:
        Universal
        
    Returns:
        boolean: True if the argument is a black stone, False if it's not
    """
    return pedra == 'X'

def eh_pedra_neutra(pedra):
    """ 	
    Check if the argument is a stone

    Args:
        Universal
        
    Returns:
        boolean: True if the argument is a stone, False if it's not
    """
    return pedra == '.'

def pedras_iguais(pedra1, pedra2):
    """ 	
    Check if the stones are equal

    Args:
        stone
        stone

    Returns:
        boolean: True if the stones are equal, False if the're not
    """
    return eh_pedra(pedra1) and eh_pedra(pedra2) and pedra1 == pedra2

def pedra_para_str(pedra):
    """ 	
    Converts a stone to a String

    Args:
        Stone

    Returns:
        string: 'X'-Black, 'O'-White or '.':-Neutra
    """
    return pedra

def eh_pedra_jogador(pedra):
    """ 	
    Check if the argument is a white or black stone

    Args:
        Universal
        

    Returns:
        boolean: True if the argument is a Black or White stone, False if it's not
    """
    return not(pedra == '.')

def cria_goban_vazio(n):
    """ 	
    Creates a blank goban

    Args:
        inter: the size of the goban, it can be 9, 13 or 19

    Returns:
        goban
    """
    if type(n) == int and n in (9, 13, 19):
        return list(list(0 for i in range(n)) for j in range(n))
    raise ValueError("cria_goban_vazio: argumento invalido")

def cria_goban(n, inter_brancas, inter_pretas):
    """ 	
    Creates a goban with stones in the indicated intersections

    Args:
        inter: the size of the goban, it can be 9, 13 or 19
        tuple: a tuple with the intersections where the white stones will be
        tuple: a tuple with the intersections where the black stones will be

    Returns:
        goban
    """
    if type(n)==int and n in (9, 13, 19) and type(inter_brancas)==tuple and type(inter_pretas)==tuple:
        pretas = ordena_intersecoes(inter_pretas)
        brancas = ordena_intersecoes(inter_brancas)
        verificadas = ()
        tab = cria_goban_vazio(n)
        for i in range(len(pretas)):
            if pretas[i] in brancas or pretas[i] in verificadas or not(eh_intersecao(pretas[i]))\
            or ord(obtem_col(pretas[i]))-64 > n or obtem_lin(pretas[i]) > n:
                raise ValueError("cria_goban: argumentos invalidos")
            tab[(ord(obtem_col(pretas[i]))-65)][obtem_lin(pretas[i])-1] = 1
            verificadas += (cria_intersecao(obtem_col(pretas[i]), obtem_lin(pretas[i])),)
        verificadas = ()
        for i in range(len(brancas)):
            if not(eh_intersecao(brancas[i])) or brancas[i] in verificadas\
            or ord(obtem_col(brancas[i]))-64 > n or obtem_lin(brancas[i]) > n:
                raise ValueError("cria_goban: argumentos invalidos")
            tab[(ord(obtem_col(brancas[i]))-65)][obtem_lin(brancas[i])-1] = 2
            verificadas += (cria_intersecao(obtem_col(brancas[i]), obtem_lin(brancas[i])),)
        return tab
    raise ValueError("cria_goban: argumentos invalidos")

        

    
def cria_copia_goban(tab):
    """ 	
    Creates a copy of a goban

    Args:
        goban

    Returns:
        goban
    """   
    tab_copy = [[element for element in column] for column in tab]
    return tab_copy
        
def obtem_ultima_intersecao(tab):
    """ 	
    Gets the last intersection(the upper right corner one) of a goban

    Args:
        goban

    Returns:
        intersection: the last one(the upper right corner one)
    """
    return (chr(len(tab)+64), len(tab[0]))

def obtem_pedra(tab, inter):
    """ 	
    Gets the stone in a intersection of a goban

    Args:
        goban
        intersction

    Returns:
        stone
    """   
    if tab[ord(obtem_col(inter))-65][obtem_lin(inter)-1] == 2:
        return 'O'
    elif tab[ord(obtem_col(inter))-65][obtem_lin(inter)-1] == 1:
        return 'X'
    else:
        return '.'

def obtem_cadeia(tab, inter):
    """ 	
    Get the chain of stones in the given intersection

    Args:
        goban
        intersection

    Returns:
        tuple: a tuple with the inersections that belong to the chains
    """   
    Resp = (inter,)
    Verif = ()
    while Resp != Verif:
        Verif = Resp
        for i in Resp:
            for j in obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(tab)):
                if not(j in Resp) and (obtem_pedra(tab, j) == obtem_pedra(tab, inter)):
                    Resp += (j,)
    return ordena_intersecoes(Resp)   


def coloca_pedra(tab, inter, pedra):
    """ 	
    Puts a stone in a given intersection of a tab

    Args:
        goban
        intersction
        stone

    Returns:
        goban
    """   
    if eh_pedra_branca(pedra):
        tab[ord(obtem_col(inter))-65][obtem_lin(inter)-1] = 2
    else:
        tab[ord(obtem_col(inter))-65][obtem_lin(inter)-1] = 1
    return tab

def remove_pedra(tab, inter):
    """ 	
    Removes a stone in a given intersection of a tab

    Args:
        goban
        intersction

    Returns:
        goban
    """   
    tab[ord(obtem_col(inter))-65][obtem_lin(inter)-1] = 0
    return tab

def remove_cadeia(tab, tup_inter):
    """ 	
    Removes a chain of stones in a given tab

    Args:
        goban
        tuple: a tuple with the intersection that belong to the chain

    Returns:
        goban
    """   
    for i in tup_inter:
        remove_pedra(tab, i)
    return tab

def eh_goban(tab):
    """ 	
    Checks if the argument is a goban

    Args:
        Universal

    Returns:
        boolean: True if the argument is a goban, and False if it's not
    """   
    if type(tab) == list and all(isinstance(listas, list) for listas in tab) and len(tab) in (9, 13, 19):
        tamanho = len(tab[0])
        for i in tab:
            if not(len(i) in (9, 13, 19) and len(i) == tamanho):
                return False
            for j in i:
                if not(j in (0, 1, 2)):
                    return False
        return True
    return False

def eh_intersecao_valida(tab, inter):
    """ 	
    Check if a intersection exists in a goban

    Args:
        goban
        intersction

    Returns:
        boolean: True if the intersection exists in a goban, False if it does not 
    """   
    return eh_intersecao(inter) and len(tab) > ord(obtem_col(inter))-65 and len(tab[0]) >= obtem_lin(inter)

def gobans_iguais(tab1, tab2):
    """ 	
    Checks if two goban are equal

    Args:
        goban
        goban

    Returns:
        boolean: True if they are equal, False if the're not
    """   
    if eh_goban(tab1) and eh_goban(tab2) and len(tab1) == len(tab2):
        for i in range(len(tab1)):
            for j in range(len(tab1[0])):
                if tab1[j][i] != tab2[j][i]:
                    return False
        return True
    return False

def goban_para_str(tab):
    """ 	
    Converts a goban into a string
    
    Args:
        goban
        
    Returns:
        string
    """   
    seq_letras = ''
    parcela = ''
    n=0
    while n != len(tab):
        seq_letras =f'{seq_letras} {chr(n+65)}' 
        n += 1
    tab = tab[::-1]
    for linha in range(len(tab[0])):
        parcela = f'{linha+1:2d}' + parcela
        for coluna in range(len(tab)):
            if tab[coluna][linha] == 0:
                parcela = '. ' + parcela
            elif tab[coluna][linha] == 1:
                parcela = 'X ' + parcela
            else:
                parcela = 'O ' + parcela
        parcela = f'\n{linha+1:2d} ' + parcela
    return f'  {seq_letras}{parcela}\n  {seq_letras}'

def obtem_territorios(tab):
    """ 	
    Gets all the territories in a goban

    Args:
        goban

    Returns:
        tuple: a tuple with all the intersections that are territories
    """   
    def obtem_cadeias(tab):
        """ 	
        Gets all the existing chains in a goban

        Args:
            goban

        Returns:
            tuple: a tuple with tuples of intersections
        """   
        inter_cadeias = ()
        cadeias = ()
        for colunas in range(len(tab)):
            for linhas in range(len(tab[0])):
                if not(cria_intersecao(chr(colunas + 65),linhas+1) in inter_cadeias) and\
                eh_pedra_neutra(obtem_pedra(tab, cria_intersecao(chr(colunas + 65),linhas+1))):
                   inter_cadeias += obtem_cadeia(tab, cria_intersecao(chr(colunas + 65),linhas+1))
                   cadeias += (obtem_cadeia(tab, cria_intersecao(chr(colunas + 65),linhas+1)),)
        return cadeias
    
    def obtem_fronteiras(tab, tup_cadeias):
        """ 	
        Gets all the borders of the chains

        Args:
            goban
            tuple: a tuple with all the tuples of intersections that are chains

        Returns:
            dictionary: a dictionary where the Keys are the chains and the Values are the respective borders
        """   
        fronteira = ()
        fronteiras = {}
        for cadeia in tup_cadeias:
            for intersecao in cadeia:
                for intersecoes_adj in obtem_intersecoes_adjacentes(intersecao, obtem_ultima_intersecao(tab)):
                    if not(intersecoes_adj in cadeia) and not(intersecoes_adj in fronteira):
                        fronteira += (intersecoes_adj,)
            fronteiras.update({cadeia: fronteira,}) 
            fronteira = ()
        return fronteiras
    #ver se a fronteira é formada unicamente por pedras da mesma cor
    def eh_territorio(tab, dict_fronteiras):
        """ 	
        Check which chains are territories

        Args:
            goban
            dictionary: a dictionary where the Keys are the chains and the Values are the respective borders

        Returns:
            tuple: a tuple with tuples of lands
        """   
        territorios = ()
        for cadeia, fronteira in dict_fronteiras.items():
            pedra_anterior = ''
            igual = 1
            for intersecao in fronteira:
                if obtem_pedra(tab, intersecao) == pedra_anterior:
                    igual += 1
                pedra_anterior = obtem_pedra(tab, intersecao)
            if igual == len(fronteira) and eh_pedra_jogador(obtem_pedra(tab, intersecao)):
                territorios += (cadeia,)
        return territorios
    
    return eh_territorio(tab, obtem_fronteiras(tab, obtem_cadeias(tab)))

def obtem_adjacentes_diferentes(tab, tup_inter):
    """ 	
    Gets the freedoms or the borders of a chain

    Args:
        goban
        tuple

    Returns:
        tuple
    """
    adjacentes = ()
    for intersecao in tup_inter:
        for intersecoes_adj in obtem_intersecoes_adjacentes(intersecao, obtem_ultima_intersecao(tab)):
            if not(intersecoes_adj in tup_inter) and not(intersecoes_adj in adjacentes) and\
            not(eh_pedra_jogador((obtem_pedra(tab, intersecao)))==eh_pedra_jogador((obtem_pedra(tab, intersecoes_adj)))):
                adjacentes += (intersecoes_adj,)
    return ordena_intersecoes(adjacentes)

def jogada(tab, inter, pedra):
    """ 	
    Makes a move in a goban

    Args:
        goban
        intersection
        stone

    Returns:
        goban
    """
    coloca_pedra(tab, inter, pedra)
    for intersecao in obtem_intersecoes_adjacentes(inter, obtem_ultima_intersecao(tab)):
        cadeia = obtem_cadeia(tab, intersecao)
        if not(obtem_adjacentes_diferentes(tab, obtem_cadeia(tab, intersecao))):
            for i in cadeia:
                remove_pedra(tab, i)
    return tab

def obtem_pedras_jogadores(tab):
    """ 	
    Gets the amount of stones each player has in a goban

    Args:
        goban

    Returns:
        tuple: where the first position is a integer with the amount of white  
         stones, and in the second another integer with the amount of black stones
    """ 
    brancas = 0
    pretas = 0
    for colunas in range(len(tab)):
        for linhas in range(len(tab[0])):
            if tab[colunas][linhas] == 2:
                brancas += 1
            elif tab[colunas][linhas] == 1:
                pretas += 1
    return (brancas, pretas)

def calcula_pontos(tab):
    """ 	
    Calculates all the points of each player in a goban

    Args:
        goban

    Returns:
        tuple: where the first position is a integer with the points 
       of white and in the second another integer with the points of black 
    """
    pontos_brancas = obtem_pedras_jogadores(tab)[0]
    pontos_pretas = obtem_pedras_jogadores(tab)[1]
    for territorio in obtem_territorios(tab):
        if eh_pedra_branca(obtem_pedra(tab, obtem_adjacentes_diferentes(tab, territorio)[0])):
            pontos_brancas += len(territorio)
        else:
            pontos_pretas += len(territorio)
    return (pontos_brancas, pontos_pretas)

def eh_jogada_legal(tab, inter, pedra, tab_controle):
    """ 	
    Checks if a move is aloud

    Args:
        goban
        intersction
        stone
        goban: this goban is the previous position of the goban

    Returns:
        boolean: True if the move is aloud, False if it's not
    """   
    def eh_suicio(tab, inter, pedra):
        """ 	
        Checks if a move leaves to a illegal state called suicide

        Args:
            goban
            intersection
            stone

        Returns:
            boolean: True if it is suicide, False if it's not
        """
        tab_apos_jogada = cria_copia_goban(tab)
        jogada(tab_apos_jogada, inter, pedra)
        inter_adj = obtem_intersecoes_adjacentes(inter, obtem_ultima_intersecao(tab_apos_jogada))
        pedras = []
        n = 0
        for i in inter_adj:
            pedras.append(obtem_pedra(tab_apos_jogada, i))
        for p in pedras:
            if eh_pedra_jogador(p) and p != pedra:
                n+=1
        return n == len(pedras)

    tab1_copia = cria_copia_goban(tab)
    jogada(tab1_copia, inter, pedra)
    if not(eh_pedra_neutra(obtem_pedra(tab, inter))) or tab1_copia == tab_controle or eh_suicio(tab, inter, pedra):
        return False
    elif eh_pedra_branca(pedra):
        if obtem_pedras_jogadores(tab1_copia)[0] <= obtem_pedras_jogadores(tab)[0]:
            return False
    elif eh_pedra_preta(pedra):
        if obtem_pedras_jogadores(tab1_copia)[1] <= obtem_pedras_jogadores(tab)[1]:
            return False
    return True

def turno_jogador(tab, pedra, tab_controle):
    """ 	
    Makes a turn of a player

    Args:
        goban
        stone
        goban: this goban is the previous position of the goban

    Returns:
        turno
    """
    while True:
        if eh_pedra_branca(pedra):
            escolha = str(input("Escreva uma intersecao ou 'P' para passar [O]:"))
        else:
            escolha = str(input("Escreva uma intersecao ou 'P' para passar [X]:"))
        if escolha == 'P':
            return False
        
        elif 1 < len(escolha) < 3 and type(escolha[0]) == str and 65<=ord(escolha[0])<=83 and 48<=ord(escolha[1])<=57 and type(int(escolha[1:])) == int and eh_intersecao_valida(tab, str_para_intersecao(escolha))\
        and eh_jogada_legal(tab, str_para_intersecao(escolha), pedra, tab_controle):
            jogada(tab, str_para_intersecao(escolha), pedra)
            return True
        
def go(n, tb, tp):
    """ 	
    This is the main function that calls all others to make the game happen

    Args:
        integer
        tuple: a tuple with the external represantation of intersections
          where the white stones would be
        tuple: a tuple with the external represantation of intersection
          where the black stones would be


    Returns:
        boolean: True if white won and False if black won or it was a draw
        """
    if type(n) == int and n in (9, 13, 19) and type(tb)==tuple and type(tp)==tuple:
        #tuple_brancas_repre_int = tuple(lambda x:str_para_intersecao(x) for x in tb)
        #tuple_pretas_repre_int = tuple(lambda x:str_para_intersecao(x) for x in tp)
        goban_teste = cria_goban_vazio(9)
        tup_b = lista_para_strings_intersecao(tb)
        tup_p = lista_para_strings_intersecao(tp)
        if not(all(eh_intersecao_valida(tab, x) for x in tb) and all(eh_intersecao_valida(tab, x) for x in tp)):
            raise ValueError("go: argumentos invalidos")
        tab = cria_goban(n, tup_b, tup_p)
        tab_anterior = cria_copia_goban(tab)
        n = 1
        passou = 0
        print(f'Branco (O) tem {calcula_pontos(tab)[0]} pontos\nPreto (X) tem {calcula_pontos(tab)[1]} pontos')
        print(goban_para_str(tab))
        while n:
            if n%2!=0:
                tab_anterior = cria_copia_goban(tab)
                if turno_jogador(tab, cria_pedra_preta(), tab_anterior) == False:
                    passou +=1
                else:
                    passou = 0
                n += 1
            else:
                if turno_jogador(tab, cria_pedra_branca(), tab_anterior) == False:
                    passou += 1
                else:
                    passou = 0
                n += 1
            if passou == 2:
                print(f'Branco (O) tem {calcula_pontos(tab)[0]} pontos\nPreto (X) tem {calcula_pontos(tab)[1]} pontos')
                print(goban_para_str(tab))
                return calcula_pontos(tab)[0] >= calcula_pontos(tab)[1]
            print(f'Branco (O) tem {calcula_pontos(tab)[0]} pontos\nPreto (X) tem {calcula_pontos(tab)[1]} pontos')
            print(goban_para_str(tab))
    raise ValueError("go: argumentos invalidos")