# 8-Puzzle Game com IA (Busca em Largura - BFS - Greedy)

## Descrição do Projeto

Este repositório contém a implementação de um jogo 8-Puzzle, onde o objetivo é organizar os números em ordem crescente, movendo os blocos em uma grade 3x3. Além do jogo, também implementamos duas abordagens de Inteligência Artificial (IA) para resolver o puzzle automaticamente:

1. **Busca em Largura (BFS - Breadth-First Search)**
2. **Algoritmo Guloso (Greedy) com Heurística de Manhattan**

Este projeto foi desenvolvido como parte da disciplina de Inteligência Artificial do curso de Engenharia de Computação, por Renan Rohers Salvador, Tiago Dallecio, e Kauai Duhamel.

## Estrutura do Repositório

O repositório contém os seguintes arquivos:

  - **IA BFS**: Resolve o puzzle automaticamente usando a técnica de Busca em Largura (BFS).
  - **IA Greedy**: Resolve o puzzle automaticamente usando um algoritmo guloso com a heurística de Manhattan.

## Funcionamento das IAs

### Busca em Largura (BFS)

A IA que utiliza a técnica de Busca em Largura (BFS) explora todos os estados possíveis do tabuleiro de maneira sistemática, garantindo que o caminho mais curto para a solução seja encontrado. O algoritmo BFS é completo, o que significa que sempre encontrará a solução se ela existir, embora possa ser menos eficiente em termos de uso de memória e tempo, especialmente para problemas maiores.

### Algoritmo Guloso (Greedy) com Heurística de Manhattan

A IA baseada no algoritmo guloso (Greedy) utiliza a heurística de Manhattan para avaliar a proximidade de um estado ao estado final. A distância de Manhattan é calculada como a soma das distâncias verticais e horizontais de cada bloco até a posição correta no tabuleiro final.

O algoritmo Greedy toma decisões baseadas em qual movimento parece o mais promissor (ou seja, aquele que minimiza a distância de Manhattan) no momento, sem garantir a solução ótima, mas frequentemente alcançando uma solução de forma rápida. 

Essa abordagem pode não encontrar o caminho mais curto até a solução, mas é geralmente mais rápida e menos intensiva em recursos do que o BFS, especialmente em problemas onde a eficiência é mais importante do que a garantia de encontrar o caminho ótimo.

## Contribuidores

Este projeto foi desenvolvido por:
- **Renan Rohers Salvador** - 22003561
- **Tiago Dallecio** - 22001336
- **Kauai Duhamel** 

## Licença

Este projeto foi desenvolvido como parte de um trabalho acadêmico e está disponível apenas para fins educacionais. Por favor, consulte os autores antes de reutilizar qualquer parte deste código.

---
