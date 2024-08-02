from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from times import Time
    from partida import Partida


class Campeonato:
    """Atributos:

    times: uma lista de objetos Time participantes do campeonato
    partidas: uma lista de objetos Partida realizadas no campeonato

    Métodos:
    adicionar_time(time: Time): adiciona um time ao campeonato.
    registrar_partida(partida: Partida): registra uma partida no campeonato.
    classificacao(): exibe a classificação dos times com base no número total de gols marcados."""

    def __init__(self) -> None:
        """Inicializa a lista de times do campeonato e a lista de partidas."""
        self.times = []
        self.partidas: List[Partida] = []

    def adicionar_time(self, time: 'Time') -> None:
        """Adiciona um time ao campeonato."""
        self.times.append(time)

    def registrar_partida(self, partida: 'Partida') -> None:
        """Registra uma partida do campeonato."""
        self.partidas.append(partida)

    def classificacao(self):
        """Exibe a classificação dos times no campeonato."""
        times_ordenados = sorted(self.times, key=lambda time: time.pontos, reverse=True)
        print('Classificação do campeonato:')
        for time in times_ordenados:
            print(f'Time: {time.nome} | Pontos: {time.pontos}')