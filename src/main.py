def montarDigrafo(dicionarioDigrafo, verticesDigrafo, maior_num):
    for origem, destino in verticesDigrafo:
        dicionarioDigrafo[origem].append(destino)
    #for x in dicionarioDigrafo:
    #    print(f"{x}:{dicionarioDigrafo[x]}")
    matriz = gerarMatriz(dicionarioDigrafo, maior_num)
    return matriz
    # print("\nMatriz de Adjacências para Dígrafo:")
    # imprimirMatriz(matriz, maior_num)

def montarGrafo(dicionarioGrafo, verticesGrafo, maior_num):
    for origem, destino in verticesGrafo:
        if origem != destino:
            dicionarioGrafo[origem].append(destino)
            dicionarioGrafo[destino].append(origem)
        else:
            dicionarioGrafo[origem].append(destino)
    #for x in dicionarioGrafo:
    #    print(f"{x}:{dicionarioGrafo[x]}")
    matriz = gerarMatriz(dicionarioGrafo, maior_num)
    return matriz
    #print("\nMatriz de Adjacências para Grafo:")
    #imprimirMatriz(matriz, maior_num)

def gerarMatriz(dicionario, maior_num):
    matriz = []
    for i in range(1, maior_num + 1):
        linha = []
        for j in range(1, maior_num + 1):
            if j in dicionario[i]:
                linha.append(1)
            else: 
                linha.append(0)
        matriz.append(linha)
    return matriz

def imprimirMatriz(matriz_grafo, matriz_digrafo, maior_num, graus, ge, gr):
    print(" ", end="")
    print("V | ", end="")
    for x in range(1, maior_num + 1):
        print(x, end=" ")
    print("Grau", end="")
    print(" | ", end=" ")
    for x in range(1, maior_num + 1):
        print(x, end=" ")
    print(" GE", end=" ")
    print("GR", end=" ")
    print("\n " + "--" * maior_num*2 + "--" * 9 )
    for i in range(maior_num):
        if i+1 < 10: 
            print(f" {i+1} | ",end="")
        else:
            print(f"{i+1} | ",end="")
            
        for j in range(maior_num):
            print(matriz_grafo[i][j], end=" ")
        print(f"  {graus.count(i+1)}  | ", end=" ")
        for m in range(maior_num):
            print(matriz_digrafo[i][m], end=" ")
        print(f" {gr.count(i+1)}", end=" ")
        print(f" {ge.count(i+1)}", end=" ")
        print()

arestas = input("Arestas do grafo (origem destino, origem destino, ...): ")
vertices = []
print("Matrizes de Adjacências para Grafo e Dígrafo (lado a lado):")
for par in arestas.split(","):
    vv = []
    for v in par.split():
        vv.append(int(v))
    vertices.append(vv)

if len(vertices) != 0:
    maior_num = vertices[0][0]
    for ar in vertices:
        for num in ar:
            if num > maior_num:
                maior_num = num
    dicionarioDigrafo = {}
    for x in range(1, maior_num + 1):
        dicionarioDigrafo[x] = []
    dicionarioGrafo = {}
    for x in range(1, maior_num + 1):
        dicionarioGrafo[x] = []
    graus = []
    for num1, num2 in vertices:
        graus.append(num1)
        graus.append(num2)
    ge = []
    gr = []
    for num1, num2 in vertices:
        ge.append(num2)
    for num1, num2 in vertices:
        gr.append(num1)


            
        
    grafo_teste = montarGrafo(dicionarioGrafo, vertices, maior_num)
    digrafo_teste = montarDigrafo(dicionarioDigrafo, vertices, maior_num)
    imprimirMatriz(grafo_teste, digrafo_teste, maior_num, graus, ge, gr)
    
else:
    print("Não existe arestas a serem analisadas")

# 3 5, 4 5, 2 6, 3 6, 5 5, 6 1, 5 2, 1 4, 1 1, 4 2, 2 3
    
    
