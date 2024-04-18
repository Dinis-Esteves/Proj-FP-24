import pytest 
import FP2324P1 as fp # <--- Change the name projectoFP to the file name with your project


class TestPublicTerritorioIntersecoes:

    def test_1(self):
        grid = ((0,1,0,0),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        assert fp.eh_territorio(grid)
    
    def test_2(self):
        grid = ((0,1,0,0),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0))
        assert not fp.eh_territorio(grid)

    def test_3(self):
        grid = ((0,1,0,0),(0,0,0,0),(0,0,1,0),(1,2,0,0),(0,0,0,0))
        assert not fp.eh_territorio(grid)

    def test_4(self):
        assert fp.eh_intersecao(('B', 25))
        
    def test_5(self):
        assert not fp.eh_intersecao((25, 'B'))
    
    def test_6(self):    
        assert not fp.eh_intersecao(('A', 200))
        
    def test_7(self):    
        grid = ((0,1,0,0),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        assert fp.eh_intersecao_livre(grid, ('A', 1))
    
    def test_8(self):    
        grid = ((0,1,0,0),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        assert not fp.eh_intersecao_livre(grid, ('A', 2))
        
    def test_9(self):    
        t = ((0,1,0,0),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        assert fp.obtem_intersecoes_adjacentes(t, ('C',3)) == (('C', 2), ('B', 3), ('D', 3), ('C', 4))

    def test_10(self):    
        t = ((0,1,0,0),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        assert fp.obtem_intersecoes_adjacentes(t, ('A',1)) == (('B', 1), ('A', 2))
   
    def test_11(self):    
        grid = ((0,1,0,0),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        assert fp.obtem_ultima_intersecao(grid) == ('E', 4)

    def test_12(self):    
        grid = ((0,1,0,0,0),(0,0,0,0,1),(0,0,1,0,1))
        assert fp.obtem_ultima_intersecao(grid) == ('C', 5)

    def test_13(self):    
        tup = (('A',1), ('A',2), ('A',3), ('B',1), ('B',2), ('B',3) )
        assert fp.ordena_intersecoes(tup) == (('A',1), ('B',1), ('A',2), ('B',2), ('A',3), ('B',3) )
    
    def test_14(self):
        t = ((0,1,0,0),(0,0,0,0))
        assert fp.territorio_para_str(t) == '   A B\n 4 . .  4\n 3 . .  3\n 2 X .  2\n 1 . .  1\n   A B'
    
    def test_15(self):
        t = t=((1,1,1,0,0,0,0,0,1,1),)
        assert fp.territorio_para_str(t) == '   A\n10 X 10\n 9 X  9\n 8 .  8\n 7 .  7\n 6 .  6\n 5 .  5\n 4 .  4\n 3 X  3\n 2 X  2\n 1 X  1\n   A'
     
    def test_16(self):
        t = ((0,1,0,0),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        assert fp.territorio_para_str(t) == '   A B C D E\n 4 . . . . .  4\n 3 . . X . .  3\n 2 X . . . .  2\n 1 . . . X .  1\n   A B C D E'
       
    def test_17(self):    
        grid = ((0,1,0,0),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        assert fp.eh_intersecao_valida(grid, ('A', 1))
    
    def test_18(self):    
        grid = ((0,1,0,0),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        assert fp.eh_intersecao_valida(grid, ('A', 2))
        
    def test_19(self):    
        grid = ((0,1,0,0),(0,0,0,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
        assert not fp.eh_intersecao_valida(grid, ('A', 50))
        
        
class TestPublicCadeiaVale:
    def test_1(self):
        t = ((1,1,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert fp.obtem_cadeia(t,('A',2)) == (('A', 1), ('A', 2), ('B', 2), ('A', 3))

    def test_2(self):
        t = ((1,1,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert fp.obtem_cadeia(t,('C',3)) == (('C', 3),)

    def test_3(self):
        t = ((1,1,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert fp.obtem_cadeia(t,('A',4)) == (('B', 1), ('C', 1), ('D', 1), ('E', 1), ('C', 2), ('D', 2), ('E', 2), ('B', 3), ('D', 3), ('E', 3), ('A', 4), ('B', 4), ('C', 4), ('D', 4), ('E', 4))

    def test_4(self):
        t = ((1,1,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert fp.obtem_vale(t,('A',1)) == (('B', 1), ('C', 2), ('B', 3), ('A', 4))
        
    def test_5(self):
        t = ((1,1,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert fp.obtem_vale(t,('C',3)) == (('C', 2), ('B', 3), ('D', 3), ('C', 4))
        
    def test_6(self):
        t = ((1,1,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        with pytest.raises(ValueError) as excinfo:
            fp.obtem_vale(t,('B',1))
        assert "obtem_vale: argumentos invalidos" == str(excinfo.value)
    

class TestPublicInfoTerritorio:
    
    def test_1(self):
        t = ((1,1,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert fp.verifica_conexao(t, ('A',1), ('A',3))
        
    def test_2(self):
        t = ((1,1,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert not fp.verifica_conexao(t, ('A',1), ('C',3))

    def test_3(self):
        t = ((1,1,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert fp.verifica_conexao(t, ('A',4), ('B',1))

    def test_4(self):
        t = ((1,1,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert fp.calcula_numero_montanhas(t) == 5

    def test_5(self):
        t = ((1,0,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert fp.calcula_numero_montanhas(t) == 4
        
    def test_6(self):
        t = ((1,1,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert fp.calcula_numero_cadeias_montanhas(t) == 2

    def test_7(self):
        t = ((1,0,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert fp.calcula_numero_cadeias_montanhas(t) == 4
        
    def test_8(self):
        t = ((1,1,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert fp.calcula_tamanho_vales(t) == 6

    def test_9(self):
        t = ((1,0,1,0),(0,1,0,0),(0,0,1,0),(0,0,0,0),(0,0,0,0))
        assert fp.calcula_tamanho_vales(t) == 7
        
    