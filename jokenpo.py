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


# Jokenpo


# Testes
class JokenpoTest(unittest.TestCase):
    
    def test_pedra_pedra(self):
       self.assertEqual(jokenpo(PEDRA, PEDRA), 'empate')


if __name__ == '__main__':
    unittest.main()
