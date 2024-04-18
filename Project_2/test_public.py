import pytest 
import sys
from proj_2 import * # <--- Change the name projectoFP to the file name with your project

class TestPublicIntersecao:

    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            i1 = cria_intersecao('a', 12)        
        assert "cria_intersecao: argumentos invalidos" == str(excinfo.value)
    
    def test_2(self):
        assert not intersecoes_iguais(cria_intersecao('A', 2), cria_intersecao('B', 13))

    def test_3(self):
        assert intersecoes_iguais(cria_intersecao('A', 2), str_para_intersecao('A2'))

    def test_4(self):
        assert intersecao_para_str(cria_intersecao('B', 13)) == 'B13'

    def test_5(self):
        i1 = cria_intersecao('A', 2)
        assert ('A1', 'B2', 'A3') == tuple(intersecao_para_str(i) for i in obtem_intersecoes_adjacentes(i1, cria_intersecao('S',19)))
        
    def test_6(self):
        tup = (cria_intersecao('A',1), cria_intersecao('A',3), cria_intersecao('B',1), cria_intersecao('B',2))
        assert ('A1', 'B1', 'B2', 'A3') == tuple(intersecao_para_str(i) for i in ordena_intersecoes(tup))
        
        
class TestPublicPedra:

    def test_1(self):
        assert  eh_pedra(cria_pedra_branca())

    def test_2(self):
        assert not pedras_iguais(cria_pedra_branca(), cria_pedra_preta())

    def test_3(self):
        b, p = cria_pedra_branca(), cria_pedra_preta()
        assert pedra_para_str(b), pedra_para_str(p) == ('O', 'X')
        
    def test_4(self):
        assert not eh_pedra_jogador(cria_pedra_neutra())
        
class TestPublicGoban:
    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            g = cria_goban_vazio(10)
        assert "cria_goban_vazio: argumento invalido" == str(excinfo.value)

    def test_2(self):
        assert eh_goban(cria_goban_vazio(9))
        
    def test_3(self):
        g = cria_goban_vazio(9)
        i1 = cria_intersecao('C',8)
        assert pedra_para_str(obtem_pedra(g,i1)) == '.'
        
    def test_4(self):
        g = cria_goban_vazio(9)
        b, p = cria_pedra_branca(), cria_pedra_preta()
        ib = 'C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'
        ip = 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'
        for i in ib: coloca_pedra(g, str_para_intersecao(i), b)
        for i in ip: coloca_pedra(g, str_para_intersecao(i), p)
        hyp = \
"""   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . X . .  7
 6 . . . . . . X . .  6
 5 . . . . X X . . .  5
 4 . . . O X X . . .  4
 3 O O O O . . . . .  3
 2 . . O O . . . . .  2
 1 . . O . . . . . .  1
   A B C D E F G H I"""
        assert goban_para_str(g) == hyp
        
    def test_5(self):
        g = cria_goban_vazio(9)
        b, p = cria_pedra_branca(), cria_pedra_preta()
        ib = 'C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'
        ip = 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'
        for i in ib: coloca_pedra(g, str_para_intersecao(i), b)
        for i in ip: coloca_pedra(g, str_para_intersecao(i), p)
        cad = obtem_cadeia(g, cria_intersecao('F',5))
        assert  tuple(intersecao_para_str(i) for i in cad) == ('E4', 'F4', 'E5', 'F5')

    def test_6(self):
        g = cria_goban_vazio(9)
        b, p = cria_pedra_branca(), cria_pedra_preta()
        ib = 'C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'
        ip = 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'
        for i in ib: coloca_pedra(g, str_para_intersecao(i), b)
        for i in ip: coloca_pedra(g, str_para_intersecao(i), p)
        cad = obtem_cadeia(g, cria_intersecao('F',5))
        liberdades = obtem_adjacentes_diferentes(g, cad)
        assert tuple(intersecao_para_str(i) for i in liberdades) == ('E3', 'F3', 'G4', 'D5', 'G5', 'E6', 'F6')
        
    def test_7(self):
        g = cria_goban_vazio(9)
        b, p = cria_pedra_branca(), cria_pedra_preta()
        ib = 'C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'
        ip = 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'
        for i in ib: coloca_pedra(g, str_para_intersecao(i), b)
        for i in ip: coloca_pedra(g, str_para_intersecao(i), p)
        terr = obtem_territorios(g)
        assert tuple(intersecao_para_str(i) for i in terr[0]) == ('A1', 'B1', 'A2', 'B2')

    def test_8(self):
        g = cria_goban_vazio(9)
        b, p = cria_pedra_branca(), cria_pedra_preta()
        ib = 'C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'
        ip = 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'
        for i in ib: coloca_pedra(g, str_para_intersecao(i), b)
        for i in ip: coloca_pedra(g, str_para_intersecao(i), p)
        terr = obtem_territorios(g)
        border = obtem_adjacentes_diferentes(g, terr[0])
        assert  tuple(intersecao_para_str(i) for i in border) == ('C1', 'C2', 'A3', 'B3')

    def test_9(self):
        g = cria_goban_vazio(9)
        b, p = cria_pedra_branca(), cria_pedra_preta()
        ib = 'C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'
        ip = 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'
        for i in ib: coloca_pedra(g, str_para_intersecao(i), b)
        for i in ip: coloca_pedra(g, str_para_intersecao(i), p)
        assert obtem_pedras_jogadores(g) == (8, 6)
        
    def test_10(self):
        ib = tuple(str_para_intersecao(i) \
            for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        ip = tuple(str_para_intersecao(i) \
            for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        g = cria_goban(9, ib, ip)
        assert goban_para_str(g) == \
"""   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . X . .  7
 6 . . . . . . X . .  6
 5 . . . . X X . . .  5
 4 . . . O X X . . .  4
 3 O O O O . . . . .  3
 2 X . O O . . . . .  2
 1 X X O . . . . . .  1
   A B C D E F G H I"""
   
    def test_11(self):
        ib = tuple(str_para_intersecao(i) \
            for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        ip = tuple(str_para_intersecao(i) \
            for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        g = cria_goban(9, ib, ip)
        b = cria_pedra_branca()
        _ = jogada(g, cria_intersecao('B', 2), b)
        assert goban_para_str(g) == \
"""   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . X . .  7
 6 . . . . . . X . .  6
 5 . . . . X X . . .  5
 4 . . . O X X . . .  4
 3 O O O O . . . . .  3
 2 . O O O . . . . .  2
 1 . . O . . . . . .  1
   A B C D E F G H I"""
   
    def test_12(self):
        ref = \
"""   A B C D E F G H I J K L M N O P Q R S
19 . . . . . . . . . . . . . . . . . . . 19
18 . . . . . . . . . . . . . . . . . . . 18
17 . . . . . . . . . . . . . . . . . . . 17
16 . . . . . . . . . . . . . . . . . . . 16
15 . . . . . . . . . . . . . . . . . . . 15
14 . . . . . . . . . . . . . . . . . . . 14
13 . . . . . . . . . . . . . . . . . . . 13
12 . . . . . . . . . . . . . . . . . . . 12
11 . . . . . . . . . . . . . . . . . . . 11
10 . . . . . . . . . . . . . . . . . . . 10
 9 . . . . . . . . . . . . . . . . . . .  9
 8 . . . . . . . . . . . . . . . . . . .  8
 7 . . . . . . . . . . . . . . . . . . .  7
 6 . . . . . . . . . . . . . . . . . . .  6
 5 . . . . . . . . . . . . . . . . . . .  5
 4 . . . . . . . . . . . . . . . . . . .  4
 3 . . . . . . . . . . . . . . . . . . .  3
 2 . . . . . . . . . . . . . . . . . . .  2
 1 . . . . . . . . . . . . . . . . . . .  1
   A B C D E F G H I J K L M N O P Q R S"""
        assert goban_para_str(cria_goban_vazio(19)) == ref
        
class TestPublicCalculaPontos:
    def test_1(self):
        ib = tuple(str_para_intersecao(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        ip = tuple(str_para_intersecao(i) for i in ('E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        g = cria_goban(9, ib, ip)
        assert calcula_pontos(g) == (12, 6)
        
class TestPublicEhJogadaLegal:
    def test_1(self):
        ib = tuple(str_para_intersecao(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        ip = tuple(str_para_intersecao(i) for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        g = cria_goban(9, ib, ip)
        l = cria_goban_vazio(9)
        b, p = cria_pedra_branca(), cria_pedra_preta()
        assert not eh_jogada_legal(g, cria_intersecao('B', 2), p, l)
        
    def test_2(self):
        ib = tuple(str_para_intersecao(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        ip = tuple(str_para_intersecao(i) for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        g = cria_goban(9, ib, ip)
        l = cria_goban_vazio(9)
        b, p = cria_pedra_branca(), cria_pedra_preta()
        assert eh_jogada_legal(g, cria_intersecao('B', 2), b, l)

    def test_3(self):
        ib = tuple(str_para_intersecao(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        ip = tuple(str_para_intersecao(i) for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        g = cria_goban(9, ib, ip)
        l = cria_goban_vazio(9)
        b, p = cria_pedra_branca(), cria_pedra_preta()
        ref = \
"""   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . X . .  7
 6 . . . . . . X . .  6
 5 . . . . X X . . .  5
 4 . . . O X X . . .  4
 3 O O O O . . . . .  3
 2 X . O O . . . . .  2
 1 X X O . . . . . .  1
   A B C D E F G H I"""
        assert (not eh_jogada_legal(g, cria_intersecao('B', 2), p, l)) \
            and eh_jogada_legal(g, cria_intersecao('B', 2), b, l) \
                and ref == goban_para_str(g)

    def test_4(self):
        ib = tuple(str_para_intersecao(i) for i in ('A2','B1','B3','C2'))
        ip = tuple(str_para_intersecao(i) for i in ('C1','C3','D1','D2'))
        b, p = cria_pedra_branca(), cria_pedra_preta()
        g = cria_goban(9, ib, ip)
        g_ko = cria_copia_goban(g)
        assert eh_jogada_legal(g, cria_intersecao('B', 2), p, g_ko)

    def test_5(self):
        ib = tuple(str_para_intersecao(i) for i in ('A2','B1','B3','C2'))
        ip = tuple(str_para_intersecao(i) for i in ('C1','C3','D1','D2'))
        b, p = cria_pedra_branca(), cria_pedra_preta()
        g = cria_goban(9, ib, ip)
        g_ko = cria_copia_goban(g)
        jogada(g, cria_intersecao('B', 2), p)   
        assert not eh_jogada_legal(g, cria_intersecao('B', 2), b, g_ko)
   
class TestPublicTurnoJogador:
    def test_1(self):
        ib = tuple(str_para_intersecao(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        ip = tuple(str_para_intersecao(i) for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        g = cria_goban(9, ib, ip)
        ref = (True, "Escreva uma intersecao ou 'P' para passar [X]:Escreva uma intersecao ou 'P' para passar [X]:Escreva uma intersecao ou 'P' para passar [X]:")
        assert turno_jogador_offline(g, cria_pedra_preta(), cria_goban_vazio(9), 'B10\nB2\nG5\n') == ref

    def test_2(self):
        ib = tuple(str_para_intersecao(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        ip = tuple(str_para_intersecao(i) for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        g = cria_goban(9, ib, ip)
        turno_jogador_offline(g, cria_pedra_preta(), cria_goban_vazio(9), 'B10\nB2\nG5\n')
        ref = \
"""   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . X . .  7
 6 . . . . . . X . .  6
 5 . . . . X X X . .  5
 4 . . . O X X . . .  4
 3 O O O O . . . . .  3
 2 X . O O . . . . .  2
 1 X X O . . . . . .  1
   A B C D E F G H I"""
        assert goban_para_str(g) == ref
   
class TestPublicGo:
    def test_1(self):
        input_str = 'A1\nB1\nB2\nA2\nA1\nA3\nA1\nC1\nE5\nP\nP\n'
        assert go_offline(9, (), (), input_str) == (False, REF_GO_PUBLIC_JOGO1)
        
    def test_2(self):
        ib = 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'B3', 'I3', 'B4', 'D4', 'E4', 'F4', 'B5', 'D5', 'G5', 'I5', 'B6', 'D6', 'E6', 'F6', 'G6', 'I6', 'C7', 'I7', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8'
        ip = 'C3', 'D3', 'E3', 'F3', 'G3', 'C4', 'G4', 'H4', 'C5', 'H5', 'C6', 'H6', 'D7', 'E7', 'F7', 'G7', 'H7'
        assert go_offline(9, ib, ip, 'E5\nF5\nE5\nP\nP\n') == (True, REF_GO_PUBLIC_JOGO2)
        

### AUXILIAR CODE NECESSARY TO REPLACE STANDARD INPUT 
class ReplaceStdIn:
    def __init__(self, input_handle):
        self.input = input_handle.split('\n')
        self.line = 0

    def readline(self):
        if len(self.input) == self.line:
            return ''
        result = self.input[self.line]
        self.line += 1
        return result

class ReplaceStdOut:
    def __init__(self):
        self.output = ''

    def write(self, s):
        self.output += s
        return len(s)

    def flush(self):
        return 


def turno_jogador_offline(board, pedra, last, input_jogo):
    oldstdin = sys.stdin
    sys.stdin = ReplaceStdIn(input_handle=input_jogo)
    
    oldstdout, newstdout = sys.stdout,  ReplaceStdOut()
    sys.stdout = newstdout

    try:
        res = turno_jogador(board, pedra, last)
        text = newstdout.output
        return res, text
    except ValueError as e:
        raise e
    finally:
        sys.stdin = oldstdin
        sys.stdout = oldstdout

def go_offline(n, ib, ip, input_jogo):
    oldstdin = sys.stdin
    sys.stdin = ReplaceStdIn(input_handle=input_jogo)
    
    oldstdout, newstdout = sys.stdout,  ReplaceStdOut()
    sys.stdout = newstdout

    try:
        res = go(n, ib, ip)
        text = newstdout.output
        return res, text
    except ValueError as e:
        raise e
    finally:
        sys.stdin = oldstdin
        sys.stdout = oldstdout

REF_GO_PUBLIC_JOGO1 = \
"""Branco (O) tem 0 pontos
Preto (X) tem 0 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 . . . . . . . . .  3
 2 . . . . . . . . .  2
 1 . . . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 0 pontos
Preto (X) tem 81 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 . . . . . . . . .  3
 2 . . . . . . . . .  2
 1 X . . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 1 pontos
Preto (X) tem 1 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 . . . . . . . . .  3
 2 . . . . . . . . .  2
 1 X O . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 1 pontos
Preto (X) tem 2 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 . . . . . . . . .  3
 2 . X . . . . . . .  2
 1 X O . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 3 pontos
Preto (X) tem 1 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 . . . . . . . . .  3
 2 O X . . . . . . .  2
 1 . O . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 3 pontos
Preto (X) tem 2 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 X . . . . . . . .  3
 2 O X . . . . . . .  2
 1 . O . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 3 pontos
Preto (X) tem 2 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 X . . . . . . . .  3
 2 O X . . . . . . .  2
 1 O O . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 0 pontos
Preto (X) tem 81 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 X . . . . . . . .  3
 2 . X . . . . . . .  2
 1 . . X . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 1 pontos
Preto (X) tem 6 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . O . . . .  5
 4 . . . . . . . . .  4
 3 X . . . . . . . .  3
 2 . X . . . . . . .  2
 1 . . X . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 1 pontos
Preto (X) tem 6 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . O . . . .  5
 4 . . . . . . . . .  4
 3 X . . . . . . . .  3
 2 . X . . . . . . .  2
 1 . . X . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 1 pontos
Preto (X) tem 6 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . O . . . .  5
 4 . . . . . . . . .  4
 3 X . . . . . . . .  3
 2 . X . . . . . . .  2
 1 . . X . . . . . .  1
   A B C D E F G H I
"""

REF_GO_PUBLIC_JOGO2 = \
"""Branco (O) tem 62 pontos
Preto (X) tem 17 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . O O O O O O O  8
 7 . . O X X X X X O  7
 6 . O X O O O O X O  6
 5 . O X O . . O X O  5
 4 . O X O O O X X .  4
 3 . O X X X X X . O  3
 2 . . O O O O O O .  2
 1 . . . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 60 pontos
Preto (X) tem 18 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . O O O O O O O  8
 7 . . O X X X X X O  7
 6 . O X O O O O X O  6
 5 . O X O X . O X O  5
 4 . O X O O O X X .  4
 3 . O X X X X X . O  3
 2 . . O O O O O O .  2
 1 . . . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 62 pontos
Preto (X) tem 17 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . O O O O O O O  8
 7 . . O X X X X X O  7
 6 . O X O O O O X O  6
 5 . O X O . O O X O  5
 4 . O X O O O X X .  4
 3 . O X X X X X . O  3
 2 . . O O O O O O .  2
 1 . . . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 51 pontos
Preto (X) tem 28 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . O O O O O O O  8
 7 . . O X X X X X O  7
 6 . O X . . . . X O  6
 5 . O X . X . . X O  5
 4 . O X . . . X X .  4
 3 . O X X X X X . O  3
 2 . . O O O O O O .  2
 1 . . . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [O]:Branco (O) tem 51 pontos
Preto (X) tem 28 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . O O O O O O O  8
 7 . . O X X X X X O  7
 6 . O X . . . . X O  6
 5 . O X . X . . X O  5
 4 . O X . . . X X .  4
 3 . O X X X X X . O  3
 2 . . O O O O O O .  2
 1 . . . . . . . . .  1
   A B C D E F G H I
Escreva uma intersecao ou 'P' para passar [X]:Branco (O) tem 51 pontos
Preto (X) tem 28 pontos
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . O O O O O O O  8
 7 . . O X X X X X O  7
 6 . O X . . . . X O  6
 5 . O X . X . . X O  5
 4 . O X . . . X X .  4
 3 . O X X X X X . O  3
 2 . . O O O O O O .  2
 1 . . . . . . . . .  1
   A B C D E F G H I
"""
