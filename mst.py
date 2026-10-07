"""Árvore Geradora Mínima (MST) com Kruskal e Prim.

Uso:
    python mst.py --input exemplos/grafo1.txt --alg kruskal
    python mst.py --input exemplos/grafo1.txt --alg prim --start A
"""
import argparse
import heapq

def carregar_grafo(caminho):
    vertices = []
    arestas = []
    with open(caminho, encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if linha == "" or linha.startswith("#"):
                continue
            u, v, p = linha.split()
            peso = float(p)
            if peso == int(peso):
                peso = int(peso)
            if u not in vertices:
                vertices.append(u)
            if v not in vertices:
                vertices.append(v)
            arestas.append((u, v, peso))
    return vertices, arestas

def lista_adjacencia(vertices, arestas):
    adj = {}
    for v in vertices:
        adj[v] = []
    for u, v, p in arestas:
        adj[u].append((v, p))
        adj[v].append((u, p))
    return adj

class UnionFind:
    def __init__(self):
        self.pai = {}
        self.rank = {}

    def make_set(self, v):
        self.pai[v] = v
        self.rank[v] = 0

    def find(self, v):
        if self.pai[v] != v:
            self.pai[v] = self.find(self.pai[v])
        return self.pai[v]

    def union(self, u, v):
        ru = self.find(u)
        rv = self.find(v)
        if ru == rv:
            return False
        if self.rank[ru] < self.rank[rv]:
            ru, rv = rv, ru
        self.pai[rv] = ru
        if self.rank[ru] == self.rank[rv]:
            self.rank[ru] += 1
        return True

def kruskal(vertices, arestas):
    uf = UnionFind()
    for v in vertices:
        uf.make_set(v)
    mst = []
    for u, v, p in sorted(arestas, key=lambda a: a[2]):
        if uf.union(u, v):
            mst.append((u, v, p))
    return mst

def prim(vertices, adj, inicio):
    visitados = set()
    mst = []
    for raiz in [inicio] + vertices:
        if raiz in visitados:
            continue
        visitados.add(raiz)
        fila = []
        for v, p in adj[raiz]:
            heapq.heappush(fila, (p, raiz, v))
        while fila:
            p, u, v = heapq.heappop(fila)
            if v in visitados:
                continue
            visitados.add(v)
            mst.append((u, v, p))
            for x, px in adj[v]:
                if x not in visitados:
                    heapq.heappush(fila, (px, v, x))
    return mst

def imprimir(nome, vertices, mst):
    print("Algoritmo:", nome)

    if len(mst) == len(vertices) - 1:
        print("Arestas escolhidas:")
        for u, v, p in mst:
            print(u, v, p)
        print("Peso total:", sum(a[2] for a in mst))
        return

    print("O grafo é DESCONEXO: não existe uma MST para todo o grafo.")
    print("Floresta geradora mínima (uma árvore por componente):")
    uf = UnionFind()
    for v in vertices:
        uf.make_set(v)
    for u, v, p in mst:
        uf.union(u, v)
    grupos = {}
    for v in vertices:
        raiz = uf.find(v)
        if raiz not in grupos:
            grupos[raiz] = []
        grupos[raiz].append(v)

    i = 1
    for comp in grupos.values():
        print()
        print("Componente", i, ":", "{" + ", ".join(comp) + "}")
        arestas_comp = [a for a in mst if a[0] in comp]
        for u, v, p in arestas_comp:
            print(u, v, p)
        print("Peso:", sum(a[2] for a in arestas_comp))
        i += 1
    print()
    print("Peso total da floresta:", sum(a[2] for a in mst))


def main():
    parser = argparse.ArgumentParser(description="MST com Kruskal ou Prim")
    parser.add_argument("--input", required=True, help="arquivo do grafo")
    parser.add_argument("--alg", required=True, choices=["kruskal", "prim"])
    parser.add_argument("--start", help="vértice inicial do Prim (padrão: primeiro lido)")
    args = parser.parse_args()

    vertices, arestas = carregar_grafo(args.input)
    if len(vertices) == 0:
        print("Grafo vazio.")
        return

    if args.alg == "kruskal":
        imprimir("Kruskal", vertices, kruskal(vertices, arestas))
    else:
        inicio = args.start if args.start else vertices[0]
        if inicio not in vertices:
            print("Vértice inicial", inicio, "não existe no grafo.")
            return
        adj = lista_adjacencia(vertices, arestas)
        imprimir("Prim", vertices, prim(vertices, adj, inicio))


if __name__ == "__main__":
    main()
