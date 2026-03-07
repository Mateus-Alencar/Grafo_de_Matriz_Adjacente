# Matriz de Adjacência de Grafos

Repositório dedicado à implementação de grafos e dígrafos utilizando matriz de adjacência. Ela incluí documentação, exemplos e código da implementação

## Sumário
graph-adjacency-matrix-implementation  
├── src/  
│   └── grafo.py  
├── examples/  
│   └──   
└── README.md  

## Conceitos

Um **Grafo** é uma estruta de dados compostas por: **Vértices**(nós) e **Areas**(conexões).
```txt
G = (V, E)
```

Um **dígrafo** (grafo direcionado) possui arestas com direção.
Exemplo:
```txt
A -> B
B -> C
C -> A
```
>[!NOTE]  
> Em caso de dúvida, consulte o [seguinte repositório](https://github.com/Mateus-Alencar/EstruturaDeDados/blob/main/DOCS/grafos.md).

### Matriz de Adjacência
>[!WARNING]
>A matriz de adjacência mostra quais vértices estão ligados entre si.  

A matriz de adjacência é uma forma de representar grafos utilizando uma matriz quadrada.

> Se um grafo possui N vértices, a matriz terá dimensão: `N x N`  

Grafo:  
![alt text](./images/Ex_Matriz_Adjacencias.png)  

`1 → existe aresta / 0 → não existe aresta`  

#### Exemplos
**Grafo**: Construção de uma lista de adjacências para cada um dos vértices. 
>[!WARNING]
> Deve ser inserido as areastas da esquerda para a direita  

Arestas: 3 5, 4 5, 2 6, 3 6, 5 5, 6 1, 5 2, 1 4, 1 1, 4 2, 2 3

Listas de adjacências
|Origem|Lista|
|------|-----| 
|1| 6 > 4 > 1    |
|2| 6 > 5 > 4 > 3|
|3| 5 > 6 > 2    |
|4| 5 > 1 > 2    |
|5| 3 > 4 > 5 > 2|
|6| 2 > 3 > 1 >  |
> No grafo, as arestas não têm direção então a aresta aparece para os dois vértices.

**Dígrafo**
Arestas: 6 1, 5 2, 2 3, 5 1, 3 5, 4 5, 2 6, 3 2, 1 6, 4 2, 2 2

|Origem|Lista|
|------|-----| 
|1| 6|
|2| 3 > 6 > 2|
|3| 5 > 2|
|4| 5 > 2|
|5| 2 > 1|
|6| 1|
> No dígrafo, as arestas têm direção. Então a aresta aparece apenas no vértice de origem.

### Matriz de incidência  
>[WARNING]  
> Matriz de incidência mostra quais vértices participam de cada aresta.

Grafo  
![alt text](./images/Ex_Matriz_Incidencia.png)  
Dígrafo  
![alt text](./images/Ex_Digrafo_Incidencia.png)  