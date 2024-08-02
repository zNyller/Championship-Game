from typing import TYPE_CHECKING
from random import randint

if TYPE_CHECKING:
    from times import Time

class Partida:
    """Atributos:

    time1: um objeto Time representando o primeiro time
    time2: um objeto Time representando o segundo time
    gols_time1: número de gols marcados pelo time1
    gols_time2: número de gols marcados pelo time2

    Métodos:
    resultado(): retorna uma representação da partida, como "Time1 vs Time2: [gols_time1] - [gols_time2]"."""

    def __init__(self, time1: 'Time', time2: 'Time') -> None:
        self.time1 = time1
        self.time2 = time2
        self.gols_time1 = randint(0, 5)
        self.gols_time2 = randint(0, 5)
        self.vencedor = None

    def resultado(self) -> str:
        """Exibe o resultado da partida."""
        print(f'{self.time1.nome} vs {self.time2.nome}: [{self.gols_time1}] - [{self.gols_time2}]')
        if self.gols_time1 > self.gols_time2:
            self.vencedor = self.time1
        elif self.gols_time1 < self.gols_time2:
            self.vencedor = self.time2
        else:
            self.vencedor = None
        print(f'Vencedor: {self.vencedor.nome}') if self.vencedor else print('Empate!')
    
    def pontuacao(self):
        if self.vencedor:
            print(f'{self.vencedor.nome} recebe 3 pontos!')
            self.vencedor.pontos += 3
        else:
            print('As duas equipes somaram 1 ponto!')
            self.time1.pontos += 1
            self.tim2.pontos += 1