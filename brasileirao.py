from random import randint
from jogador import Jogador
from times import Time
from partida import Partida
from campeonato import Campeonato


class Brasileirao:
    """Classe principal. Gerencia os times e as partidas do campeonato."""

    CLUBES = [
        'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Botafogo',
        'Corinthians', 'Criciúma', 'Cruzeiro', 'Cuiabá', 'Flamengo',
        'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventude',
        'Palmeiras', 'RB Bragantino', 'São Paulo', 'Vasco', 'Vitória'
    ]
    JOGADORES = {
        'Anthoni': 'GK', 'Fabrício': 'GK', 'Ivan': 'GK', 'Rochet': 'GK',
        'Gabriel Mercado': 'ZAG', 'Igor Gomes': 'ZAG', 'Robert Renan': 'ZAG', 'Vitão': 'ZAG',
        'Bustos': 'LD', 'Bernabei': 'LE', 'Renê': 'LE',
        'Bruno Gomes': 'VOL', 'Rômulo': 'VOL', 'Fernando': 'VOL', 
        'Bruno Henrique': 'MLG', 'Hyoran': 'MLG', 'Thiago Maia': 'MLG',
        'Gabriel Carvalho': 'MAT', 'Alan Patrick': 'MAT', 
        'Gustavo Prado': 'PE', 'Wanderson': 'PE', 'Wesley': 'PD',
        'Enner Valência': 'CA', 'Lucas Alário': 'CA', 'Lucca': 'CA', 'Rafael Borré': 'CA', 
    }

    def __init__(self) -> None:
        self.meu_clube = None
        self.clubes = self.CLUBES
        self.meus_jogadores = self.JOGADORES
        self.campeonato = Campeonato()

    def _menu(self) -> None:
        """Exibe o menu para iniciar o jogo."""
        print(f'Lista de times do Brasileirão Série A:')
        self.campeonato.classificacao(label=False)

    def _escolher_time(self):
        """Exibe a opção para o usuário escolher uma equipe."""
        while True:
            meu_time = input('Qual time você deseja coordenar? ')
            if meu_time in self.clubes:
                print(f'\nVocê irá coordenar o {meu_time}!')
                self.meu_clube = Time(meu_time)
                break
            print('Time inexistente. Escolha novamente!')
            continue
        
    def _contratar_jogadores(self):
        if self.meu_clube.nome == 'Internacional':
            for meu_jogador, pos in self.meus_jogadores.items():
                jogador = Jogador(meu_jogador, pos)
                self.meu_clube.contratar_jogador(jogador)
        else:
            while True:
                print('Crie os jogadores para o seu time! [0] para encerrar: ')
                nome = input('Nome: ')
                if nome == '0':
                    break
                posicao = input('Posição: ')
                jogador = Jogador(nome, posicao)
                self.meu_clube.contratar_jogador(jogador)

    def _realizar_partida(self):
        """Seleciona um adversário aleatório para jogar contra."""
        sorteio_time = randint(0, 19)
        self.adversario = self.campeonato.times[sorteio_time]
        self.partida = Partida(self.meu_clube, self.adversario)
        self.partida.resultado()
        self.partida.pontuacao()

    def main(self) -> None:
        """Loop principal do jogo."""
        self._menu()
        self._escolher_time()
        self._contratar_jogadores()
        self.meu_clube.listar_jogadores()

        for clube in self.clubes:
            self.campeonato.adicionar_time(clube)

        self._realizar_partida()

        print()

        self.campeonato.registrar_partida(self.partida)
        self.campeonato.classificacao()


br = Brasileirao()
br.main()