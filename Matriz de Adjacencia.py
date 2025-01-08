
class Graph:
    def __init__(self, num_vertices):
        """Inicializa o grafo com uma matriz de adjacência."""
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, v1, v2, weight=1):
        """Adiciona uma aresta entre v1 e v2 com um peso opcional."""
        self.adj_matrix[v1][v2] = weight
        self.adj_matrix[v2][v1] = weight  # Para grafos não direcionados

    def remove_edge(self, v1, v2):
        """Remove a aresta entre v1 e v2."""
        self.adj_matrix[v1][v2] = 0
        self.adj_matrix[v2][v1] = 0  # Para grafos não direcionados

    def is_adjacent(self, v1, v2):
        """Verifica se existe uma aresta entre v1 e v2."""
        return self.adj_matrix[v1][v2] != 0

    def display(self):
        """Exibe a matriz de adjacência."""
        for row in self.adj_matrix:
            print(row)

# Criando um grafo com 5 vértices
grafo = Graph(5)

# Adicionando arestas
grafo.add_edge(0, 1)
grafo.add_edge(0, 4, weight=2)
grafo.add_edge(1, 2)

# Exibindo a matriz de adjacência
print("Matriz de Adjacência:")
grafo.display()

# Verificando adjacência
print("\nAresta entre 0 e 1:", grafo.is_adjacent(0, 1))
print("Aresta entre 0 e 3:", grafo.is_adjacent(0, 3))

# Removendo uma aresta
grafo.remove_edge(0, 1)
print("\nMatriz após remover a aresta entre 0 e 1:")
grafo.display()
