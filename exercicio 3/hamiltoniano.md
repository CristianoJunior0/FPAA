**Algoritmo do Caminho Hamiltoniano**

Este projeto implementa o algoritmo de backtracking para encontrar um Caminho Hamiltoniano em um grafo usando Python.

Um Caminho Hamiltoniano é um caminho que visita todos os vértices exatamente uma vez.
É um problema clássico da Teoria dos Grafos e está relacionado ao Problema do Caixeiro Viajante.

Exemplo de grafo utilizado:
grafo = {
    0: [1, 3],
    1: [0, 2, 3],
    2: [1, 3],
    3: [0, 1, 2]
}

**Como executar**

1.Salve o código no arquivo main.py.

2.Execute no terminal:

_python main.py_

3.O programa mostrará se encontrou um Caminho Hamiltoniano.

***Exemplo de saída:***

_Caminho Hamiltoniano encontrado: [0, 1, 2, 3]_

ou

_Nenhum caminho Hamiltoniano encontrado._

**Complexidade Computacional**
***Classes de Complexidade (P, NP, NP-Completo e NP-Difícil)***

***O problema do Caminho Hamiltoniano pertence à classe NP-completo, porque:***

Está na classe NP: uma solução pode ser verificada rapidamente (em tempo polinomial).

***É tão difícil quanto outros problemas NP-completos, como o Problema do Caixeiro Viajante (TSP).**

Não há algoritmo conhecido que o resolva em tempo polinomial.

Complexidade Assintótica de Tempo

O algoritmo usa backtracking, testando várias combinações possíveis de vértices.
Em um grafo com n vértices, a complexidade é aproximadamente:

**𝑂(𝑛!)**

Isso ocorre porque o algoritmo pode testar todas as permutações possíveis de vértices.

**Método Utilizado**

A complexidade foi determinada por contagem de operações e análise combinatória,
considerando que o algoritmo tenta todas as possíveis ordens de visitação dos vértices.
Não há recorrência simples para aplicar o Teorema Mestre.

**Aplicação do Teorema Mestre**

O Teorema Mestre não se aplica neste caso, porque o algoritmo não é de divisão e conquista,
mas sim de busca exaustiva com backtracking.
Ele não divide o problema em subproblemas de mesmo tamanho.

**Casos de Complexidade**

***Melhor caso: o caminho é encontrado logo nas primeiras tentativas.***
***→ Tempo muito menor que o total de permutações.***

***Pior caso: o algoritmo precisa testar todas as combinações possíveis (O(n!)).***

***Caso médio: depende da densidade do grafo e da ordem em que os vértices são escolhidos.***

***O desempenho melhora em grafos densos (mais conexões) e piora em grafos esparsos.***

**Exemplo de Execução**

Entrada:

grafo = {
    0: [1, 3],
    1: [0, 2, 3],
    2: [1, 3],
    3: [0, 1, 2]
}


Saída:

_Caminho Hamiltoniano encontrado: [0, 1, 2, 3]_

**Conclusão**

O algoritmo implementado cumpre o objetivo de verificar e encontrar Caminhos Hamiltonianos.
Embora seja eficiente apenas para grafos pequenos, ele ilustra bem o funcionamento de algoritmos NP-completos e o uso de backtracking em busca de soluções exatas.