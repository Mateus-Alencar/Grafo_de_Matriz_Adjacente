class Grafo:
  def __init__(self, vertices):
    self.vertices = vertices
    self.lista_adjacente = []

  def montar_lista_adjacências(self):
    # Separar cada par usando a vírgula.
    for par in self.vertices.split(","):
      # par.strip() -> Remove espaços extras no começo e fim da string
      # .split() -> divide a string em uma lista usando o espaço como separador
      # map(int) aplica a função int() em cada elemento da lista
      a, b = map(int, par.strip().split())
      self.lista_adjacente.append({a: b})
    print(self.lista_adjacente)
    self.montarGrafo()
    self.montarDigrafo()

  def montarGrafo(self):
    lista = self.lista_adjacente
    DicionarioGrafo = {}
    if len(self.lista_adjacente) != 0:
      if lista:
        todos_numeros = []
        for num in lista:
          for chave, valor in num.items():
            # extend() -> serve para adicionar múltiplos elementos a uma lista
            todos_numeros.extend([chave, valor])
        maior_vertice = max(todos_numeros)
      print(maior_vertice)
      for x in range(1, maior_vertice):
        DicionarioGrafo[x] = []
      print(DicionarioGrafo)

    else:
      print("A Lista está vazia")

  def montarDigrafo(self):
    if len(self.lista_adjacente) != 0:
      pass
    else:
      print("A Lista está vazia")
    pass

print("--------------------------------------------------------------------")
print("Implementação de matriz de adjacências para grafos e dígrafos.")
vertices = input("Informe as arestas do grafo (origem destino,origem destino, ...): ")

montarLista = Grafo(vertices)
montarLista.montar_lista_adjacências()

print("----------------------------- Execução -----------------------------")
print("Matriz de Adjacências para Grafo:")
print("""
V |
-------
""")
print("Matriz de Adjacências para Dígrafo:")
print("""
V |
-------
""")



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
    print(maior_num)
else:
    print("Não existe arestas a serem analisadas")