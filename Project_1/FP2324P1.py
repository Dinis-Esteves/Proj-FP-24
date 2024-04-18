# This is the Python script for your project

def eh_territorio(land):
    """A funcao verifica se o tuple inserido cumpre os parametros para ser considerado territorio

        Este primeiro if faz as verificações inicias, se e tuple e se esta dentro do tamamho 
        aceite, em caso contrario retorna falso de imediato
        
        eh_territorio(tuple) --> boolean"""
    if type(land) != tuple or (26<len(land) or len(land)<1) or type(land[0]) !=tuple or (99<len(land[0]) or len(land[0])< 1):
        return False
    tamanho = len(land[0])

    """ Este for verifica se todos os tuples têm o mesmo tamanho e se apenas contêm 0 e 1, 
        por fim retornando True se tudo estiver de acordo"""
    for i in land:
        if type(i) != tuple or len(i) != tamanho:
            return False
        for j in i:
            if j not in (0,1):
                return False
    return True

def obtem_ultima_intersecao(land):
    """Esta funcao retorna a ultima intercao, que corresponde a ultima letra e o ultimo numero
    
    obtem_ultima_intersecao(tuple) --> tuple"""
    return (chr(len(land)+64), len(land[0]))

def eh_intersecao(inter):
    """Esta funcao verifica se o input e uma intersecao, verificando se e um tuple e se tem as letras
      e os numeros no limite imposto, caso nao se verifique retorna false
      
      eh_intersecao(tuple) --> boolean"""
    if type(inter) != tuple or len(inter) != 2 or type(inter[0]) != str or len(inter[0]) != 1 or 90<ord(inter[0]) or ord(inter[0])<65 or type(inter[1]) != int or not(99>=inter[1]>0):
        return False
    return True

def eh_intersecao_valida(land, inter):
    """Esta funcao verifica se a intersecao existe no terreno
    
    eh_intersecao_valida(tuple, tuple) --> boolean"""
    letra_max = len(land)+64
    num_max = len(land[0])
    if letra_max<ord(inter[0]) or ord(inter[0])<65 or num_max > 99 or num_max<inter[1] or inter[1]<1:
        return False
    return True

def eh_intersecao_livre(land, inter):
    """Esta funcao verifica se a posicao pedida tem uma montanha ou nao, retornando falso em caso de ter
    
    eh_intersecao_livre(tuple, tuple) --> boolean"""
    letra = land[ord(inter[0])-65]
    if letra[inter[1]-1] == 0:
        return True
    return False

def obtem_intersecoes_adjacentes(land, inter):
    """Esta funcao calcula todas as intercecoes adjacentes e verifica quais delas pertencem ao terreno,
    retornando um tuple com todas as pertencentes por ordem de leitura
    
    obtem_cadeias_adjacentes(tuple, tuple) --> tuple"""
    if eh_intersecao_valida(land, inter) == False:
        return () 
    inter_adj_cima = (inter[0], inter[1] + 1)
    inter_adj_baixo = (inter[0], inter[1] - 1)
    inter_adj_esquerda = (chr(ord(inter[0])-1), inter[1])
    inter_adj_direita = (chr(ord(inter[0])+1), inter[1])
    inter_adj = ()
    for i in (inter_adj_baixo, inter_adj_esquerda, inter_adj_direita, inter_adj_cima):
        if eh_intersecao_valida(land, i) == True:
            inter_adj += (i,)
    return inter_adj

def ordena_intersecoes(tup_inter):
    """Esta funcao ordena primeiramente por letra todas as intersecoes e de seguida corre varias vezes o codigo
    colocando em cada loop os numeros correspondentes no tuple res, retornando-o quando tiver o mesmo tamanho que o original
    
    ordena_intersecoes(tuple) --> tuple"""
    res = ()
    n = 1
    while len(tup_inter) != len(res):
        for i in sorted(tup_inter):
            if i[1] == n:
                res += (i,)
        n += 1
    return res

def territorio_para_str(land):
    """Esta funcao recebe um territorio e verifica se e, retornando um erro em caso contrario, 
    depois realiza a conversao de tuple para string que representa visualmente a matriz
    
    territorio_para_str(tuple) --> string"""
    if eh_territorio(land) == False:
        raise ValueError("territorio_para_str: argumento invalido")
    seq_letras = ''
    parcela = ''
    n=0
    while n != len(land):
        seq_letras =f'{seq_letras} {chr(n+65)}'
        n += 1
    land = land[::-1]
    for linha in range(len(land[0])):
        parcela = f'{linha+1:2d}' + parcela
        for coluna in range(len(land)):
            if land[coluna][linha] == 0:
                parcela = '. ' + parcela
            else:
                parcela = 'X ' + parcela
        parcela = f'\n{linha+1:2d} ' + parcela
    return f'  {seq_letras}{parcela}\n  {seq_letras}'
     
def obtem_cadeia(land, inter):
    """Esta funcao recebe um territorio e uma intersecao, caso algum dos argumentos seja
    invalido ou a intersecao nao seja valida naquele territorio a funcao retorna erro, caso
    contrario ela determina a cadeia e retorna um tuple com todas as intersecoes pertencentes
    
    obtem_cadeia(tuple, tuple) --> tuple"""
    if eh_territorio(land) == False or eh_intersecao(inter) == False or eh_intersecao_valida(land, inter) == False:
        raise ValueError("obtem_cadeia: argumentos invalidos")
    Resp = (inter,)
    Verif = ()
    while Resp != Verif:
        Verif = Resp
        for i in Resp:
            for j in obtem_intersecoes_adjacentes(land, i):
                if not(j in Resp) and (eh_intersecao_livre(land, j) == eh_intersecao_livre(land, inter)):
                    Resp += (j,)
    return ordena_intersecoes(Resp)

def obtem_vale(land, inter):
    """Esta funcao retorna as intercoes pertencentes ao vale da montanha, reotornando erro no caso de
    algum arguento estar errado
    
    obtem_vale(tuple, tuple) --> tuple"""
    if eh_territorio(land) == False or eh_intersecao(inter) == False or eh_intersecao_valida(land, inter)==False or eh_intersecao_livre(land, inter) == True:
        raise ValueError("obtem_vale: argumentos invalidos")
    vale = ()
    for i in obtem_cadeia(land, inter):
        for j in obtem_intersecoes_adjacentes(land, i):
            if eh_intersecao_livre(land, j) == True and not(j in vale):
                vale += (j,)
    return ordena_intersecoes(vale)
    
def verifica_conexao(land, inter1, inter2):
    """Esta funcao verifica se duas intersecoes num dado territorio estao conectadas,
    retornando um erro caso algum argumento esteja errado
    
    verifica_conexao(tuple, tuple, tuple) -> boolean"""
    if eh_territorio(land)==False or eh_intersecao(inter1)==False or eh_intersecao(inter2)==False\
    or eh_intersecao_valida(land, inter1)==False or eh_intersecao_valida(land, inter2)==False:
        raise ValueError("verifica_conexao: argumentos invalidos")
    return inter2 in obtem_cadeia(land, inter1)

def calcula_numero_montanhas(land):
    """Esta funcao retorna o numero de montanhas no territorio, caso o argumento dado
    nao seja um territorio a funcao retorna um erro
    
    calcula_numero_montanhas(tuple) --> int"""
    if eh_territorio(land) == False:
        raise ValueError("calcula_numero_montanhas: argumento invalido")
    montanhas = 0
    for i in territorio_para_str(land):
        if i == 'X':
            montanhas += 1
    return montanhas

def calcula_numero_cadeias_montanhas(land):
    """Esta funcao recebe um territorio e devolve o numero de cadeias de montanhas
    existentes nesse mesmo territorio, devolvendo um erro caso o argumento 
    esteja invalido.
    
    calcula_numero_cadeias_montanhas(tuple) --> int"""
    if eh_territorio(land)==False:
        raise ValueError("calcula_numero_cadeias_montanhas: argumento invalido")
    verificadas = ()
    cadeias = 0
    for coluna in range(len(land)):
        for linha in range(len(land[0])):
            if eh_intersecao_livre(land, (chr(coluna+65), linha+1)) == False and not(obtem_cadeia(land, (chr(coluna+65), linha+1)) in verificadas):
                verificadas += (obtem_cadeia(land, (chr(coluna+65), linha+1)),)
                cadeias += 1
    return cadeias

def calcula_tamanho_vales(land):
    """Esta funcao recebe um territorio e retorna o tamanho dos vales existentes
    nesse mesmo territorio, devolvendo erro caso o argumento esteja invalido.
    
    calcula_tamanho_vales(tuple) --> int"""
    if eh_territorio(land) == False:
        raise ValueError("calcula_tamanho_vales: argumento invalido")
    todos_vales = ()
    Resp = ()
    for coluna in range(len(land)):
        for linha in range(len(land[0])):
            if eh_intersecao_livre(land, (chr(coluna+65), linha+1)) == False and not(obtem_vale(land, (chr(coluna+65), linha+1,)) in todos_vales):
                    todos_vales += (ordena_intersecoes(obtem_vale(land, (chr(coluna+65), linha+1))),)
    """Como o tuple todos_vales vai ter membros repetidos, estes for iram
    colocar todos os elementos num outro tuple, mas sem repetidos."""
    for i in todos_vales:
        for j in i:
            if not(j in Resp):
                Resp += (j,)
    return len(Resp)
