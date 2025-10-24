**MaxMin Select Algorithm**

Este projeto implementa o algoritmo MaxMin Select, que encontra simultaneamente o maior e o menor elemento de uma lista usando a técnica de divisão e conquista.

O método é mais eficiente que a busca simples, pois realiza menos comparações.

***Como funciona o algoritmo***

O algoritmo divide a lista de elementos em duas partes menores, encontra o máximo e o mínimo de cada metade recursivamente e depois combina os resultados:

***Divisão: a lista é dividida ao meio.***

***Conquista: o algoritmo encontra o maior e o menor em cada metade.***

***Combinação: compara os resultados das duas metades para definir o maior e o menor final.***

**Se a lista tiver:**

1 elemento → ele é tanto o maior quanto o menor.

2 elementos → faz uma comparação direta entre eles.

O método reduz o número de comparações totais de 
2𝑛 − 2 para aproximadamente 3𝑛/2 − 2.

**Como executar**

Salve o código no arquivo main.py.

***Execute no terminal:***

_python main.py_


O programa pedirá uma sequência de números ou usará uma lista padrão.

***Exemplo de saída:***

Lista: [4, 2, 9, 1, 7]
Menor elemento: 1
Maior elemento: 9

**Complexidade Assintótica — Contagem de Operações**

Em cada etapa o algoritmo divide o problema em duas partes e combina os resultados.

Cada comparação entre elementos é contada como uma operação.

Para n elementos, o total de comparações é aproximadamente:

𝐶(𝑛) = 3𝑛/2 − 2

Portanto, a complexidade temporal é:

𝑂(𝑛)

A complexidade é linear, pois o número de comparações cresce proporcionalmente ao tamanho da entrada.

Complexidade Assintótica — Teorema Mestre

A recorrência do algoritmo é:

𝑇(𝑛) = 2𝑇(𝑛/2) + 𝑂(1)

Identificando os parâmetros:

𝑎 = 2 → duas chamadas recursivas

𝑏 = 2 → cada chamada tem metade do tamanho

𝑓(𝑛) = 𝑂(1) → custo constante na combinação

Cálculo de 
𝑝 = log 𝑏
    𝑎
2=1

Segundo o Teorema Mestre, se 
𝑓
(
𝑛
)
=
𝑂
(
𝑛
𝑝
)
f(n)=O(np), temos:

T(n)=O(n)

Portanto, a complexidade final é linear, confirmando a análise anterior.

Casos de Complexidade

Melhor caso: lista com poucos elementos → faz poucas comparações.

Pior caso: lista grande, mas ainda linear (O(n)).

Caso médio: semelhante ao pior caso, pois o algoritmo percorre toda a lista.

O desempenho é estável, já que o número de comparações não muda drasticamente.

Conclusão

O algoritmo MaxMin Select encontra o maior e o menor elementos de forma eficiente, com complexidade O(n).
A abordagem de divisão e conquista reduz o número de comparações em relação à busca tradicional.