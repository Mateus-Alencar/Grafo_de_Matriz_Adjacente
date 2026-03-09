class Grafo:
  def __init__(self, vertices):
    self.vertices = vertices

  def montar_lista_adjacências(self):
    resultado = []
    # Separar cada par usando a vírgula.
    for par in self.vertices.split(","):
      # par.strip() -> Remove espaços extras no começo e fim da string
      # .split() -> divide a string em uma lista usando o espaço como separador
      # map(int) aplica a função int() em cada elemento da lista
      a, b = map(int, par.strip().split())
      resultado.append({a: b})
  def montarGrafo(self):
    pass
  def montarDigrafo(self):
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


# Código reutilizável
# quantidadeLista = len(resultado)
# for x in range(1, quantidadeLista + 1):
# print(x)