from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from jogador import Jogador

class Time:
    """Atributos:

    nome: nome do time
    jogadores: uma lista de objetos Jogador que representam os jogadores do time.

    Métodos:
    contratar_jogador(): adiciona um jogador à lista de jogadores do time.
    listar_jogadores(): lista todos os jogadores do time.
    total_gols(): retorna o total de gols marcados por todos os jogadores do time."""

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.jogadores: List[Jogador] = []
        self.pontos = 0

    def contratar_jogador(self, jogador: 'Jogador') -> None:
        """Contrata um jogador para o time."""
        self.jogadores.append(jogador)

    def listar_jogadores(self) -> None:
        """Lista os jogadores do time."""
        print()
        print(f'Lista de Jogadores do {self.nome}:')
        for jogador in self.jogadores:
            print(f'- {jogador.nome} | {jogador.posicao}')
        print()

    def total_gols(self) -> None:
        """Exibe o total de gols do time."""
        for jogador in self.jogadores:
            print(jogador.gols)

    def somar_pontos(self, pontos) -> None:
        self.pontos += pontos

    def retornar_pontos(self) -> int:
        print(f'Retornando pontos: {self.pontos}')
        return self.pontos