import random
import math
from collections import Counter
from music21 import note, stream
import itertools

                                ##########################################
                                #             FUNÇÃO OBJETIVO            #
                                ##########################################
def lempel_ziv_complexity_list(seq):
    '''
    Calcula a complexidade lempel-ziv de uma lista qualquer.
    
    Parâmetros:
    
    seq (list): Uma lista qualquer.
    
    Retorna: 
    int: O número de complexidade que vai de 1 ao infinito.
    '''
    n = len(seq) #n = tamanho da sequência
    i = 0 #Index que determina o fim de uma sublista
    complexity = 1 #Complexidade inicial
    while i < n - 1: #Cria um laço de repetição que só acaba quando i chega ao final da lista
        sub_list = seq[0:i+1]
        k = 1
        while i + k < n and seq[i + k] in sub_list:
            k += 1
        i += k
        if i < n:
            complexity += 1
    return complexity

def shannon_entropy(seq):
    '''
    Calcula a entropia de Shannon de uma lista.
    
    Parâmetro:
    
    seq (list): Uma lista qualquer.
    
    Retorna:
    
    float: Entropia de Shannon
    '''
    # Conta a frequência de cada elemento na sequência
    freq = Counter(seq)
    # Calcula as probabilidades de cada elemento
    n = len(seq)
    prob = [qnt / n for qnt in freq.values()]
    # Calcula a entropia de shannon
    entropy = -sum(p * math.log2(p) for p in prob)
    return entropy

def func_obj(seq):
    '''
    Calcula a fração de entropia/complexidade de uma dada lista. Utilza das seguintes funções:
    - lempel_ziv_complexity_list
    - shannon_entropy
    
    Parâmetros: 
    
    seq(list): Uma lista qualquer.
    
    Retorna: 
    
    float: O valor de entropia/complexidade.
    '''
    entropia = shannon_entropy(seq)
    complexidade = lempel_ziv_complexity_list(seq)
    
    a = entropia/complexidade
    return a

                                ##########################################
                                #    GERAÇÃO DE INDIVÍDUO E POPULAÇÃO    #
                                ##########################################

def gene_music():
    '''
    Escolhe uma nota musical aleatória.
    As notas possíveis são:
    Null (Intervalo), C, C# (sustenído), D, D#, E, F, F#, G, A, A#, B.
    '''
    notes = ['Null','C', 'C#','D','D#','E','F','F#','G','G#','A','A#','B']
    gene = random.choice(notes)
    return gene
    
def candidato_music(n):
    '''
    Cria um arranjo de notas musicais aleatórias.
    
    Parâmetos:
    
    n (int): Um número inteiro que define a quantidade de notas numa música.
    
    Retorna:
    candidato (list): Uma lista de tamanho n que contém notas musicais definidas na função 'gene_music'.
    '''
    candidato = []
    for _ in range(n):
        gene = gene_music()
        candidato.append(gene)
    return candidato

def populacao_music(tamanho, n):
    '''
    Cria uma população de músicas.
    
    Parâmetros:
    
    tamanho (int): Um número inteiro que define quantos candidatos a população possui.
    n (int): Um número inteiro que define a quantidade de notas numa música.
    
    Retorna:
    populacao (list): retorna uma lista de músicas.
    '''
    populacao = []
    for _ in range(tamanho):
        populacao.append(candidato_music(n))
    return populacao

                                ##########################################
                                #             CRUZAMENTO                 #
                                ##########################################
def tesoura_segmentos(music, n):
    '''
    Secciona uma lista em uma lista de listas.
    
    Parâmetros:
    music(list): Uma lista.
    n: Tamanho dos segmentos.
    
    Retorna:
    Uma lista dos segmentados da lista original.
    '''
    return [music[i:i + n] for i in range(0, len(music), n)]

def cruzamento_semi_heuristico(music_p, music_m, n, chance_cruzamento):
    '''
    Realiza um cruzamento entre duas músicas. Os filhos são resultado de segmentos de genes cruzados entre os pais.
    Esse cruzamento toma em conta a entropia e complexidade dos segmentos.
    
    Parâmetros:
    music_p(list): Um candidato
    music_m(list): Outro candidato
    n(int): Tamanho do segmentos. Recomenda-se usar um inteiro que tenha candidato como múltiplo
    chance_cruzamento(float): Um número entre 0 e 1.
    
    Retorna:
    filho_entropia(list): Uma lista de notas musicais que tem os segmentos mais entrópicos do pai e mãe alternados
    filho_lempel(list): Uma lista de notas musicais que tem os segmentos com menor complexidade do pai e mãe alternados
    '''
    if random.random() < chance_cruzamento:
        # Segmentação
        segmentos_pai = tesoura_segmentos(music_p, n)
        segmentos_mae = tesoura_segmentos(music_m, n)
        
        # Cálculo de entropias e complexidades
        entropias_pai = [shannon_entropy(s) for s in segmentos_pai]
        entropias_mae = [shannon_entropy(s) for s in segmentos_mae]
        lempelziv_pai = [lempel_ziv_complexity_list(s) for s in segmentos_pai]
        lempelziv_mae = [lempel_ziv_complexity_list(s) for s in segmentos_mae]
        
        # Segmentos ordenados por entropia e complexidade
        seg_entr_pai = sorted(zip(entropias_pai, segmentos_pai), key=lambda x: x[0], reverse=True)
        seg_entr_mae = sorted(zip(entropias_mae, segmentos_mae), key=lambda x: x[0], reverse=True)
        seg_lempel_pai = sorted(zip(lempelziv_pai, segmentos_pai), key=lambda x: x[0])
        seg_lempel_mae = sorted(zip(lempelziv_mae, segmentos_mae), key=lambda x: x[0])
        
        # Segmentos ordenados por entropia e complexidade
        seg_order_entr_pai = [pair[1] for pair in seg_entr_pai]
        seg_order_entr_mae = [pair[1] for pair in seg_entr_mae]
        seg_order_lempel_pai = [pair[1] for pair in seg_lempel_pai]
        seg_order_lempel_mae = [pair[1] for pair in seg_lempel_mae]
        
        # Garantir que a mistura use o comprimento da menor lista
        min_length = min(len(seg_order_entr_pai), len(seg_order_entr_mae), len(seg_order_lempel_pai), len(seg_order_lempel_mae))
        
        # Misturando segmentos de entropia e complexidade de pais e mães
        mistura_entropy = []
        mistura_lempel = []
        for i in range(min_length):
            if i % 2 == 0:
                mistura_entropy.append(seg_order_entr_pai[i])
                mistura_lempel.append(seg_order_lempel_mae[i])
            else:
                mistura_entropy.append(seg_order_entr_mae[i])
                mistura_lempel.append(seg_order_lempel_pai[i])

        # Garantir que as misturas estejam no tamanho correto
        filho_entropia = list(itertools.chain(*mistura_entropy))[:len(music_p)]
        filho_lempel = list(itertools.chain(*mistura_lempel))[:len(music_p)]
        
        return filho_entropia, filho_lempel
    else:
        return music_p, music_m

                                ##########################################
                                #                MUTAÇÃO                 #
                                ##########################################
                
import random

def mutacao_ritmica(populacao, CHANCE_DE_MUTACAO):
    """
    Essa função tem a chance de alterar de 3 formas diferentes a população dada previamente.
    
    Argumentos:
    população: lista de indivíduos (lista) gerados aleatoriamente.
    CHANCE_DE_MUTACAO: float que limita a probabilidade de ocorrer uma mutação em cada indivíduo da população.
    """

    notes = ['Null', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']  # Definindo as possíveis notas musicais.

    for individuo in populacao:
        if random.random() < CHANCE_DE_MUTACAO:
            gene = random.randint(2, len(individuo) - 3)  # Esse intervalo de 2 a len(individuo) - 3 é para garantir espaço para mutações

            # Mutação 1: Troca a nota atual por uma nova nota aleatória
            available_notes = notes.copy()
            available_notes.remove(individuo[gene])  # Removendo da lista de notas, a nota que correspondia originalmente a esse gene
            individuo[gene] = random.choice(available_notes)  # Sorteando uma nota nova

            # Mutação 2: Inverte uma pequena subseção do indivíduo, sem alterar o tamanho
            subseq_start = random.randint(2, len(individuo) - 5)  # Escolher um ponto de partida seguro para a subseção
            subseq_end = subseq_start + 3  # Tamanho fixo de 3 elementos para a inversão
            individuo[subseq_start:subseq_end] = reversed(individuo[subseq_start:subseq_end])

            # Mutação 3: Permuta duas notas, mantendo o tamanho do indivíduo
            idx1, idx2 = random.sample(range(2, len(individuo) - 2), 2)  # Escolher dois índices distintos para permutação
            individuo[idx1], individuo[idx2] = individuo[idx2], individuo[idx1]

    return populacao

                
    
                                ##########################################
                                #            FUNÇÃO DE SELEÇÃO           #
                                ##########################################
                
def selecao_grammy(populacao):
    """ 
    Seleciona os melhores indivíduos com base em uma divisão 8/2/2, 80% dos individuos com a 
    com o melhor fitness, 20% dos individuos com a maior entropia de shannon e 20% com menor
    complexidade de lempel-zip.

    Argumentos:
    população: lista de individuos gerados aleatóriamente segundo um padãro de geração.     
            
    """
    
    musicas_selecionadas = [] # População nova que será passada em diante. 


    fitness_ordenado = sorted(populacao, key=func_obj, reverse=True) 
    #Ordena a população do individuo com maior fitness ao menor.
    shannon_ordenado = sorted(populacao, key=shannon_entropy, reverse=True) 
    #Ordena a população do individuo com maior entropia de Shannon ao menor.
    lempel_ordenado = sorted(populacao, key=lempel_ziv_complexity_list) 
    #Ordena a população do individuo com menor complexidade de lempel-zip ao com maior.
    
    musicas_selecionadas = fitness_ordenado[:int(len(populacao) * 0.6)] + shannon_ordenado[:int(len(populacao) * 0.2)] + lempel_ordenado[:int(len(populacao) * 0.2)]

    return musicas_selecionadas
                
                                ##########################################
                                #           OUTRAS FUNÇÕES               #
                                ##########################################

def mostrar_musica(musica):
    '''
    Mostra a música reproduzida em midi.
    
    Parâmetros:
    musica (list): Uma lista de notas musicais que devem estar no padrão gerado na função 'gene_music'
    '''
    s = stream.Stream()
    for mnote in musica:
        if mnote == 'Null':
            n = note.Rest(quarterLength=0.5)
            s.append(n)
        if mnote == 'C':
            n = note.Note('C4', quarterLength=0.5)
            s.append(n)
        if mnote == 'C#':
            n = note.Note('C#4', quarterLength=0.5)
            s.append(n)
        if mnote == 'D':
            n = note.Note('D4', quarterLength=0.5)
            s.append(n)
        if mnote == 'D#':
            n = note.Note('D#4', quarterLength=0.5)
            s.append(n)
        if mnote == 'E':
            n = note.Note('E4', quarterLength=0.5)
            s.append(n)
        if mnote == 'F':
            n = note.Note('F4', quarterLength=0.5)
            s.append(n)
        if mnote == 'F#':
            n = note.Note('F#4', quarterLength=0.5)
            s.append(n)
    s.show('midi')