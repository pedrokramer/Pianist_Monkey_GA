<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Ilumlogo.pdf/page1-1200px-Ilumlogo.pdf.jpg" alt="logo_ilum" width="200"/>
<h1 align="center"> Macaco Pianista Infinito </h1>

## Bem-vindo(a)!

"Imagine um macaco pianista que escolhe teclas aleatórias num piano por um tempo indefinido. Eventualmente, ele irá tocar todas as músicas que já foram ou já serão inventadas em todo o mundo." 

Nesse repositório, desenvolvemos um Algoritmo Genético que, a partir de uma população inicial de canções, gera novas músicas de maneira a encontrar a melhor. Como parâmetro para a qualidade da melodia, utilizamos a razão entropia/complexidade. Para mais detalhes, vide seção [inserir seção]. 

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
+ Além das variáveis, é possível manipular as funções responsáveis pela Função Objetivo, 

</p>
</details>

<details>
    
<summary>Funções</summary>

  O arquivo 'funcoes_musicais.py' Contém  todas as funções necessárias para a execução do algoritmo. Sua execução é dividida em 4 etapas principais, sendo elas:


  ### Função Objetivo

Para a definição da Função Objetiva a ser utilizada, partimos da premissa de que "Uma música agradável terá uma alta entropia ". A veracidade ou não dessa premissa sob a perspectiva dos músicos não é de nosso interesse no momento. Essa premissa nos oferece um ponto de partida para a  Para mensurar essas qualidades de complexidade e entropia, [Complexidade de Lempel-Ziv](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv_complexity) e [Entropia de Shannon](https://en.wikipedia.org/wiki/Entropy_(information_theory)) 
  
  ### Seleção
  A partir dos parâmetros iniciais definidos, o algoritmo realiza a criação de 
  
  ### Cruzamento
  ### Mutação
  ### Atualização do Hall da Fama

</p>
</details>

<details>
<summary>Algoritmo Genético</summary>

O arquivo [Trabalho_gene.ipynb](https://github.com/pedrokramer/Pianist_Monkey_GA/blob/main/Trabalho_gene.ipynb) contém a arquitetura do Algoritmo Genético desenvolvido. 


</p>
</details>

