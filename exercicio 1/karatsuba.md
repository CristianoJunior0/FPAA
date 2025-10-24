Karatsuba Multiplication Algorithm

Este projeto implementa o algoritmo de multiplicação de Karatsuba em Python.
O método de Karatsuba é um algoritmo eficiente para multiplicar números grandes, reduzindo a complexidade em comparação à multiplicação tradicional.

Como funciona o algoritmo

O algoritmo utiliza a técnica de divisão e conquista:

Se os números são pequenos (menores que 10), multiplica diretamente.

Caso contrário:

Divide os números em duas partes: alta e baixa.

Calcula três multiplicações recursivas:

ac (partes mais significativas)

bd (partes menos significativas)

(a+b)(c+d) para calcular o termo do meio.

Combina os resultados para obter o produto final.

A complexidade assintótica do algoritmo é O(n^log₂3) ≈ O(n^1.585), melhor que o método tradicional O(n²).


Como executar

Clone este repositório ou copie o código.

Salve o arquivo como karatsuba.py.

Execute em um terminal



Complexidade Ciclomática

A complexidade ciclomática (M) é calculada pela fórmula:

M=E−N+2P

Onde:

E = número de arestas do grafo

N = número de nós

P = número de componentes conectados (1 neste caso)

Para a função karatsuba:

N = 11 nós

E = 12 arestas

P = 1 componente

Substituindo:

M = 12 − 11 + 2(1) = 3

Portanto, a complexidade ciclomática é M = 3.

O código possui baixa complexidade, indicando simplicidade no controle de fluxo.

São necessários 3 casos de teste para cobrir todos os caminhos:

Caso 1: x < 10 (condição verdadeira).

Caso 2: y < 10 (condição verdadeira).

Caso 3: Ambos ≥ 10 (condição falsa, executa fluxo completo).

