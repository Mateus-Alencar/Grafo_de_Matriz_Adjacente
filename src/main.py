def montarDigrafo(dicionarioDigrafo, verticesDigrafo, maior_num):
    for origem, destino in verticesDigrafo:
        dicionarioDigrafo[origem].append(destino)
    for x in dicionarioDigrafo:
        print(f"{x}:{dicionarioDigrafo[x]}")
    
    
def montarGrafo(dicionarioGrafo, verticesGrafo, maior_num):
    for origem, destino in verticesGrafo:
        if origem != destino:
            dicionarioGrafo[origem].append(destino)
            dicionarioGrafo[destino].append(origem)
        else:
            dicionarioGrafo[origem].append(destino)
    for x in dicionarioGrafo:
        print(f"{x}:{dicionarioGrafo[x]}")
    
    print("    ", end="")    
    for x in range(1, maior_num + 1):
        print(f"{x}", end=" ")
    print(f"\nV |" + "--" * maior_num)
    
print("--------------------------------------------------------------------")
print("Implementação de matriz de adjacências para grafos e dígrafos.")
arestas = input("Informe as arestas do grafo (origem destino,origem destino, ...): ")
vertices = []
# .split() -> divide a string em uma lista usando (,) como separador
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


    montarDigrafo(dicionarioDigrafo, vertices, maior_num)
    montarGrafo(dicionarioGrafo, vertices, maior_num)
    
else:
    print("Não existe arestas a serem analisadas")
    
    
    