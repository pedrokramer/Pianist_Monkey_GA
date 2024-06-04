<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Ilumlogo.pdf/page1-1200px-Ilumlogo.pdf.jpg" alt="logo_ilum" width="200"/>
<h1 align="center"> Macaco Pianista </h1>

## Bem-vindo(a)!

"Imagine um macaco pianista que escolhe teclas aleatórias num piano por um tempo indefinido. Eventualmente, ele irá tocar todas as músicas que já foram ou já serão inventadas em todo o mundo."

Nesse repositório, desenvolvemos um Algoritmo Genético que, a partir de uma população inicial de canções, gera novas músicas de maneira a encontrar o melhor indivíduo possível segundo um parâmetro de qualidade pré-estabelecido. Como parâmetro para a qualidade da melodia, utilizamos a razão entropia/complexidade. Para mais detalhes, vide seção *Funções*. 

Esse repositório de GitHub foi desenvolvido na matéria de Redes Neurais e Algoritmos Genéticos no terceiro semestre da faculdade Ilum Escola de Ciência. Matéria essa ministrada pelo professor [Daniel Cassar](https://github.com/drcassar). O trabalho deste repositório é equivalente ao trabalho final da disciplina de Algoritmos Genéticos, e fora desenvolvido pelos alunos:
+ [Pedro Kramer](https://github.com/pedrokramer) - 23013
+ [Iasodara Lima](https://github.com/Iasodara) - 23005
+ [Daniel Bravin](https://github.com/MrBravin) - 23020

<details>
    
<summary>Comece por aqui!</summary>

Todas as funções necessárias para a utilização do algoritmo estão disponíveis no arquivo `funcoes_musicais.py`, sendo necessários os seguintes Módulos/Bibliotecas:

+ Random
+ Math
+ Collections
+ itertools
+ Music21

O arquivo 'Trabalho_gene.ipynb' contém a estrutura do algoritmo desenvolvida, com parâmetros pré-definidos como exemplo de utilização. 

### Observações

+ É possível alterar a variável 'NUM_NOTAS' para gerar canções mais longas. No entanto, sugerimos a utilização de até 200 notas, dado que acima desse número o resultado não converge. 
+ Os genes devem ser múltiplos de 10 para o funcionamento adequado do algoritmo durante as etapas de Cruzamento e Mutação.

</p>
</details>

<details>
    
<summary>Arquitetura e Funções</summary>

  O arquivo `funcoes_musicais.py` Contém  todas as funções necessárias para a execução do algoritmo, que pode ser dividido em cinco etapas principais, sendo elas:

  ## Função Objetivo

Para a definição da Função Objetivo a ser utilizada, partimos da premissa de que "Uma música agradável terá um equilíbrio de uma alta entropia e uma alta complexidade". A veracidade ou não dessa premissa sob a perspectiva dos músicos não é de nosso interesse no momento, dado que essa premissa nos oferece um ponto de partida para a aplicação de um algoritmo genético. 

Para medir as qualidades de complexidade e entropia, utilizamos a [Complexidade de Lempel-Ziv](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv_complexity) e a [Entropia de Shannon](https://en.wikipedia.org/wiki/Entropy_(information_theory)). Após calcular esses valores para cada indivíduo, a função objetivo é definida como a razão entre a entropia e a complexidade. 
  
  ## Seleção
  *Indivíduos:* Os indíviduos consistem em listas de tamanho definido pela variável 'NUM_NOTAS', cujos elementos são sorteados a partir de uma lista de notas musicais. 
  
  *Gene:* Os genes de cada indivíduo consistem em conjuntos formados pela sequência de notas. 
  
  A partir dos parâmetros iniciais definidos, o algoritmo realiza a criação de uma população de indivíduos (melodias) inicial. 
  
  A seleção de indivíduos para a próxima geração é feita numa proporção 8/2/2, sendo 80% os indivíduos com maior razão entropia/complexidade, 20% indivíduos com a maior entropia e 20% indivíduos com a maior complexidade. 
  
  ## Cruzamento

  lorem ipsum
  
  ## Mutação
  
Para cada indivíduo de uma geração, é sorteada um valor entre -1 e 1. Se esse valor for menor que a probabilidade de uma mutação, o indivíduo sofre uma mutação que altera simultaneamente a sequência de notas de três formas distintas, sendo elas:

### Permutação
O algoritmo seleciona duas notas do indivíduo e troca as duas de posição entre si.
### Troca
O algoritmo seleciona uma nota do indivíduo e troca por outra nota qualquer.
### Inversão
O algoritmo seleciona uma sequência de três notas e inverte ela com a sequência de três notas anteriores. 
  
  ## Atualização do Hall da Fama
  
Durante cada nova geração, o algoritmo seleciona os indivíduos com os maiores valores da Função Objetivo e os adiciona ao Hall da Fama. Esse Hall da Fama contém os melhores resultados encontrados pelo algoritmo e o seu valor de *fitness*.


</p>
</details>

