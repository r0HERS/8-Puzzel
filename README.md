# 8-Puzzle Game com IA (BFS, DFS, Greedy, A*)

## Descrição do Projeto

Este repositório contém a implementação de um jogo 8-Puzzle, onde o objetivo é organizar os números em ordem crescente, movendo os blocos em uma grade 3x3. Além do modo de jogo manual, implementamos quatro abordagens de Inteligência Artificial (IA) para resolver o puzzle automaticamente:

1. **Busca em Largura (BFS - Breadth-First Search)**
2. **Busca em Profundidade (DFS - Depth-First Search)**
3. **Algoritmo Guloso (Greedy) com Heurística de Manhattan**
4. **Algoritmo A* (A-star) com Heurística de Manhattan**

Este projeto foi desenvolvido como parte da disciplina de Inteligência Artificial do curso de Engenharia de Computação, por Renan Rohers Salvador, Tiago Dallecio, e Kauai Duhamel.

## Estrutura do Repositório

O repositório contém os seguintes arquivos:

  - **IA BFS**: Resolve o puzzle automaticamente utilizando a técnica de Busca em Largura.
  - **IA DFS**: Resolve o puzzle utilizando a técnica de Busca em Profundidade.
  - **IA Greedy**: Resolve o puzzle automaticamente utilizando um algoritmo guloso com a heurística de Manhattan.
  - **IA A***: Resolve o puzzle utilizando o algoritmo A* com a heurística de Manhattan.
  - **Jogo Manual**: Permite que o usuário jogue e resolva o puzzle manualmente, contando o tempo de resolução e o número de movimentos realizados.

## Funcionamento das IAs

### Busca em Largura (BFS)

A IA que utiliza a técnica de Busca em Largura (BFS) explora todos os estados possíveis do tabuleiro de maneira sistemática, garantindo que o caminho mais curto para a solução seja encontrado. O algoritmo BFS é completo, o que significa que sempre encontrará a solução se ela existir, embora possa ser menos eficiente em termos de uso de memória e tempo, especialmente para problemas maiores.

### Busca em Profundidade (DFS)

A IA que utiliza a técnica de Busca em Profundidade (DFS) explora um caminho até o fim antes de retroceder e explorar outros caminhos. O DFS é eficiente em termos de memória, mas pode acabar explorando longos caminhos desnecessários antes de encontrar uma solução. Ele não garante a solução ótima, e pode levar mais tempo que o BFS em casos específicos.

### Algoritmo Guloso (Greedy) com Heurística de Manhattan

A IA baseada no algoritmo guloso (Greedy) utiliza a heurística de Manhattan para avaliar a proximidade de um estado ao estado final. A distância de Manhattan é calculada como a soma das distâncias verticais e horizontais de cada bloco até a posição correta no tabuleiro final.

O algoritmo Greedy toma decisões baseadas no movimento que minimiza a distância de Manhattan no momento, sem garantir a solução ótima, mas geralmente alcança uma solução de forma rápida. Essa abordagem pode não encontrar o caminho mais curto até a solução, mas é mais rápida e eficiente em termos de recursos.

### Algoritmo A* (A-star)

O algoritmo A* combina as vantagens da busca em largura (BFS) e do algoritmo guloso (Greedy), utilizando tanto a heurística de Manhattan quanto o custo acumulado para chegar ao estado atual. Dessa forma, o A* garante encontrar a solução ótima (menor caminho), sendo eficiente tanto em tempo quanto em recursos, sempre que possível. 

## Funcionamento do Jogo Manual

Além dos modos de IA, o jogo permite que o usuário jogue manualmente, movendo os blocos com cliques. Durante o jogo, são contabilizados o tempo de resolução e o número de movimentos, que são exibidos quando o puzzle é concluído. O jogador também pode reiniciar o jogo a qualquer momento.

## Contribuidores

Este projeto foi desenvolvido por:
- **Renan Rohers Salvador** - 22003561
- **Tiago Dallecio** - 22001336
- **Kauai Duhamel**

## Licença

Este projeto foi desenvolvido como parte de um trabalho acadêmico e está disponível apenas para fins educacionais. Por favor, consulte os autores antes de reutilizar qualquer parte deste código.

---

### Atualizações recentes

- Adição do modo **Busca em Profundidade (DFS)** e **Algoritmo A* (A-star)**.
- Modo de jogo manual agora contabiliza o **tempo de resolução** e o **número de lances**.
- Melhorias na interface para exibir as informações sobre tempo e lances para todos os modos.
