''' -------------------------- CONSTANTES -----------------------------'''

# quantidade de blocos por modelo de navio
CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}

# frotas de cada pais
PAISES =  {
    'Brasil': {
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }, 
    'França': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    },
    'Austrália': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    },
    'Rússia': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    },
    'Japão': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    }
}

paises = ['Brasil', 'Austrália', 'Japão', 'Rússia', 'França']

# alfabeto para montar o nome das colunas
ALFABETO = 'ABCDEFGHIJ'

# cores para o terminal
CORES = {
    'reset': '\u001b[0m',
    'red': '\u001b[31m',
    'black': '\u001b[30m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m'
}

''' -------------------------- FUNÇÕES -----------------------------'''

def cria_mapa (numero):
    lista = [' ']*numero
    for i in range (len(lista)):
        lista [i] = [' ']*numero

    return lista

def posicao_suporta (mapa, blocos, linha,coluna, orientação):
    if orientação=='v':
        if linha + blocos > len(mapa):
            return False
        
        for i in range(blocos):
            if mapa[linha+i][coluna]!= ' ':
                return False
            
    else:
        if coluna + blocos > (len(mapa[linha])):
            return False
        
        for i in range(blocos):
            if mapa[linha][coluna+i]!=' ':
                return False
    return True


import random
def aloca_navios(mapa,lista):
    for bloco in lista:
        erro = False

        while not erro:
            linha = random.randint(0, len(mapa)-1)
            coluna = random.randint(0,len(mapa)-1)
            orientacao = random.choice(['h', 'v'])
            funcao = posicao_suporta(mapa, bloco, linha, coluna, orientacao)

            if funcao:
                if orientacao == 'v':
                    for i in range(bloco):
                        mapa[linha+i][coluna] = 'N'
                    erro = True
                else:
                    for a in range(bloco):
                        mapa[linha][coluna + a] = 'N'
                    erro = True
    return mapa

def foi_derrotado (matriz):
    for linha in matriz:
        if 'N' in linha:
            return False
    return True

def print_mapa():
    pass

def print_tabuleiro(mapa):
    print('\n     A B C D E F G H I J')
    numero_coluna = 1
    for lista_linha in mapa:
        linha_printada = []
        for ch in lista_linha:
            if ch == 'N':
                linha_printada.append(CORES['green'] + '▒' + CORES['reset'])
            else:
                linha_printada.append(ch)
        linha_printada = ' '.join(linha_printada)
        if numero_coluna == 10:
            print(f' {numero_coluna}  {linha_printada} {numero_coluna}')
        else:
            print(f' {numero_coluna}   {linha_printada}  {numero_coluna}')
        numero_coluna += 1

import time
import sys
def loading():
    total = 100
    width = 20  # Define a largura da barra de progresso como 20 caracteres
    for i in range(0, total + 1):
        time.sleep(0.03)  # Ajuste o valor para tornar a barra de loading mais rápida
        percent = i * 100 // total
        filled_length = int(width * i // total)  # Número de caracteres '='
        progress_bar = "[" + "=" * filled_length + " " * (width - filled_length) + "]"
        
        bg = u"\u001b[47m"  # fundo
        white_text = u"\u001b[37m"  # Texto branco
        reset_color = u"\u001b[0m"  # Resetar a cor
        
        sys.stdout.write(u"\u001b[1000D")  # Move o cursor para o início da linha
        sys.stdout.write(f"{bg}{white_text}Progresso: {percent}% {progress_bar}{reset_color}")
        sys.stdout.flush()
    print("\nConcluído!")
    time.sleep(1)
    
''' -------------------------- JOGO -----------------------------'''
while True:
    print('\n')
    loading()
    print('\n========================= ' + CORES['magenta'] + 'BATALHA NAVAL - HELENA E GEORGIA '
        + CORES['reset'] + '=========================')
    time.sleep(1)

    # print bonito do dicionario 
    for pais in PAISES:
        dicionario = PAISES[pais]
        print(f'\n{pais}:')
        for navio in dicionario:
            numero = dicionario[navio]
            print(f'  {numero} {navio}')
    print()
    while True:
        país_player = input('Qual país você quer jogar?  ')
        if país_player in paises:
            break
        else:
            print('este país não está disponível')

    print('Você escolheu a nação ' + país_player)
    paises.remove(país_player)
    país_computador = random.choice(paises).capitalize()
    print('Agora é sua vez de alocar seus navios de guerra\n')

    player_mapa = cria_mapa(10)
    # TODO: print mapa
    print_tabuleiro(player_mapa)

    # alocar navios
    blocos = []
    for navio in PAISES[país_player]:
        quantidade = PAISES[país_player][navio]
        numero_blocos = CONFIGURACAO[navio]
        for vezes in range(quantidade):
            blocos.append(numero_blocos)
    print('\nNavios a alocar: ', blocos)

    for bloco in blocos:
        while True:
            linha = input('\nInforme a Linha:  ')
            letra = input('Informe a Letra:  ').upper()
            orientacao = input('Informe a Orientação  [v|h]:  ')
            
            numeros =  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
            # checa se ta certo
            if letra in ALFABETO and linha in numeros and orientacao in 'vh':
                colunas = {
                    'A': 0,
                    'B': 1,
                    'C': 2,
                    'D': 3,
                    'E': 4,
                    'F': 5,
                    'G': 6,
                    'H': 7,
                    'I': 8,
                    'J': 9
                }
                linha = int(linha)
                linha -= 1
                funcao = posicao_suporta(player_mapa, bloco, linha, colunas[letra], orientacao)
                i = 0 
                if funcao:
                    for j in range(bloco):
                        if orientacao == 'v':
                            player_mapa[linha + i][colunas[letra]] = 'N'
                            i += 1
                        else:
                            player_mapa[linha][colunas[letra] + i] = 'N'
                            i += 1
                    # TODO: print mapa
                    print_tabuleiro(player_mapa)
                    break
                else:
                    print(f'Não foi possível alocar o navio em: {letra}{linha + 1} {orientacao}')
            else:
                print('Input inválido')

    blocos_comp = []
    for navio in PAISES[país_computador]:
        quantidade = PAISES[país_computador][navio]
        numero_blocos = CONFIGURACAO[navio]
        for vezes in range(quantidade):
            blocos_comp.append(numero_blocos)

    # aloca navios computador
    mapa_comp = cria_mapa(10)
    aloca_navios(mapa_comp, blocos_comp)
    outro_comp_mapa = cria_mapa(10)
    
    while True:
        linha = input('\nInforme a Linha:  ')
        letra = input('Informe a Letra:  ').upper()
        
        numeros =  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        # checa se ta certo
        if letra in ALFABETO and linha in numeros:
            colunas = {
                'A': 0,
                'B': 1,
                'C': 2,
                'D': 3,
                'E': 4,
                'F': 5,
                'G': 6,
                'H': 7,
                'I': 8,
                'J': 9
            }
            linha = int(linha)
            linha -= 1
            if mapa_comp[linha][colunas[letra]] == 'N':
                outro_comp_mapa[linha][colunas[letra]] = CORES['red'] + '▒' + CORES['reset']
                # mapa do computador não vai mais ter N para checar se foi derrotado
                mapa_comp[linha][colunas[letra]] = ' '
            else:
                # água
                outro_comp_mapa[linha][colunas[letra]] = CORES['blue'] + '▒' + CORES['reset']
            print('\nCOMPUTADOR - ' + país_computador)
            print_tabuleiro(outro_comp_mapa)
            
            funcao = foi_derrotado(mapa_comp)
            if funcao:
                print('\nVoce ganhou!!')
                break
            
            linha2 = random.randint(0, len(mapa_comp)-1)
            coluna2 = random.randint(0,len(mapa_comp)-1)

            if player_mapa[linha2][coluna2] == 'N':
                player_mapa[linha2][coluna2] = CORES['red'] + '▒' + CORES['reset']
            else:
                # água
                player_mapa[linha2][coluna2] = CORES['blue'] + '▒' + CORES['reset']
            print('\nJOGADOR')
            print_tabuleiro(player_mapa)

            funcao = foi_derrotado(player_mapa)
            if funcao:
                print('\nVoce perdeu!!')
                break
        else:
            print('Input inválido')

    jogar_novamente = input('\n> Reiniciar Jogo?  [s|n] ')
    if jogar_novamente == 'n':
        break
    else:
        continue
    # ira reiniciar tudo
