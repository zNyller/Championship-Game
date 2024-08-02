from jogador import Jogador
from times import Time
from partida import Partida
from campeonato import Campeonato


def main():
    while True:
        jogador_nome = input('Crie um jogador! \nNome: ')
        jogador_posicao = input('Posição: ')
        print('\nJogador criado!\n')
        jogador2_nome = input('Crie outro jogador! \nNome: ')
        jogador2_posicao = input('Posição: ')
        time1 = input('\nCrie um time!\nNome: ')
        time2 = input('\nCrie outro time!\nNome: ')
        continuar = input('Continuar? ').upper()
        if continuar != 'S':
            break

    jogador1 = Jogador(jogador_nome, jogador_posicao)
    time1 = Time(time1)
    time1.contratar_jogador(jogador1)
    time1.listar_jogadores()
    jogador1.marcar_gol()
    jogador1.estatisticas()

    print()

    jogador2 = Jogador(jogador2_nome, jogador2_posicao)
    time2 = Time(time2)
    time2.contratar_jogador(jogador2)
    time2.listar_jogadores()
    jogador2.estatisticas()

    print()

    partida = Partida(time1, time2)
    partida.resultado()
    partida.pontuacao()

    print()

    brasileirao = Campeonato()
    brasileirao.adicionar_time(time1)
    brasileirao.adicionar_time(time2)
    brasileirao.registrar_partida(partida)
    brasileirao.classificacao()


main()