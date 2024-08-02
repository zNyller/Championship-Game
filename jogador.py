from times import Time

"""Desafio: Gerenciador de Times de Futebol

Criar um sistema para gerenciar times de futebol, jogadores e partidas. 
O sistema deve permitir a adição de times, a contratação de jogadores, 
a realização de partidas e a exibição de estatísticas.
"""

class Jogador:
    """Atributos:

    nome: nome do jogador
    posicao: posição do jogador (ex: Atacante, Meio-campista, Zagueiro, Goleiro)
    gols: número de gols marcados pelo jogador (inicialmente 0).

    Métodos:
    marcar_gol(): incrementa o número de gols do jogador em 1.
    estatisticas(): retorna uma representação do jogador, como "Nome: [nome], Posição: [posicao], Gols: [gols]"."""

    def __init__(self, nome: str, posicao: str) -> None:
        self.nome = nome
        self.posicao = posicao
        self.gols = 0

    def marcar_gol(self) -> None:
        """Adiciona um gol para o jogador."""
        self.gols += 1

    def estatisticas(self) -> str:
        """Exibe as estatísticas do jogador."""
        print(f'Nome: [{self.nome}], Posição: [{self.posicao}], Gols: [{self.gols}]')