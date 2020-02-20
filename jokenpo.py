"""
Jokenpo é uma brincadeira japonesa, onde dois jogadores escolhem um dentre três possíveis itens: Pedra, Papel ou Tesoura.

O objetivo é fazer um juiz de Jokenpo que dada a jogada dos dois jogadores informa o resultado da partida.

As regras são as seguintes:
    Pedra empata com Pedra e ganha de Tesoura
    Tesoura empata com Tesoura e ganha de Papel
    Papel empata com Papel e ganha de Pedra

Fonte: http://dojopuzzles.com/
"""

import unittest

# Atribuições
PEDRA = 1
PAPEL = 2
TESOURA = 3
EMPATE = 4
JOGADAS_POSSIVEIS = [PEDRA, PAPEL, TESOURA]

# Jokenpo
def validacao(jogada):
    return jogada in JOGADAS_POSSIVEIS

def jokenpo(jogada1, jogada2):
    if (not validacao(jogada1) or not validacao(jogada2)):
        return 'Jogada invalida'
    if (jogada1 == PEDRA and jogada2 == TESOURA) or (jogada1 == TESOURA and jogada2 == PEDRA):
        return PEDRA
    elif (jogada1 == PAPEL and jogada2 == TESOURA) or (jogada1 == TESOURA and jogada2 == PAPEL):
        return TESOURA
    elif (jogada1 == PAPEL and jogada2 == PEDRA) or (jogada1 == PEDRA and jogada2 == PAPEL):
        return PAPEL
    elif (jogada1 == jogada2):
        return EMPATE
    return jogada1 == jogada2    


# Testes
class JokenpoTest(unittest.TestCase):
    
    # EMPATES
    def test_pedra_empate(self):
       self.assertEqual(jokenpo(PEDRA, PEDRA), EMPATE)

    def test_papel_empate(self):
        self.assertEqual(jokenpo(PAPEL, PAPEL), EMPATE)

    def test_tesoura_empate(self):
        self.assertEqual(jokenpo(TESOURA, TESOURA), EMPATE)

    # VITÓRIAS
    def test_tesoura_papel_deve_ganhar_tesoura(self):
        self.assertEqual(jokenpo(PAPEL, TESOURA), TESOURA)

    def test_papel_tesoura_deve_ganhar_tesoura(self):
        self.assertEqual(jokenpo(TESOURA, PAPEL), TESOURA)
    
    def test_pedra_tesoura_deve_ganhar_pedra(self):
        self.assertEqual(jokenpo(TESOURA, PEDRA), PEDRA)

    def test_tesoura_pedra_deve_ganhar_pedra(self):
        self.assertEqual(jokenpo(PEDRA, TESOURA), PEDRA)

    def test_papel_pedra_deve_ganhar_papel(self):
        self.assertEqual(jokenpo(PAPEL, PEDRA), PAPEL)
    
    def test_pedra_papel_deve_ganhar_papel(self):
        self.assertEqual(jokenpo(PEDRA, PAPEL), PAPEL)

    # Erro
    def test_opcao_invalida(self):
        self.assertEqual(jokenpo(-1, -1), 'Jogada invalida')

if __name__ == '__main__':
    unittest.main()
