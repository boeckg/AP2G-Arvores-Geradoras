# Árvore Geradora Mínima – Kruskal e Prim

Implementação dos algoritmos de **Kruskal** e **Prim** para encontrar a Árvore Geradora Mínima (MST) de um grafo não direcionado e ponderado, em Python 3 puro.

## Descrição

Projeto desenvolvido como **Atividade Prática 2** da disciplina de Grafos (UFSM). O programa lê um grafo de um arquivo texto, executa o algoritmo escolhido e mostra as arestas da MST e o peso total.

Destaques:

- **Kruskal** com Union-Find (`make_set`, `find`, `union`) otimizado com **compressão de caminho** e **união por rank**.
- **Prim** com fila de prioridade (`heapq`).
- **Grafos desconexos:** o programa avisa que não existe MST para o grafo inteiro e mostra a **floresta geradora mínima**, com uma árvore por componente.
- Aceita pesos inteiros ou reais.

## Instalação

Requer apenas **Python 3**. Não há dependências externas, porque são usados só `argparse` e `heapq`, da biblioteca padrão.

```bash
git clone https://github.com/boeckg/AP2G-Arvores-Geradoras.git
cd arvore-geradora-minima-kruskal-prim
```

## Uso

```bash
python mst.py --input exemplos/grafo1.txt --alg kruskal
python mst.py --input exemplos/grafo1.txt --alg prim --start A
```

| Argumento | Obrigatório | Descrição |
|---|---|---|
| `--input` | sim | Arquivo do grafo |
| `--alg` | sim | `kruskal` ou `prim` |
| `--start` | não | Vértice inicial do Prim (padrão: primeiro vértice do arquivo) |

### Formato do arquivo

O arquivo tem uma aresta por linha, no formato `VERTICE_1 VERTICE_2 PESO`. Linhas vazias e linhas que começam com `#` são ignoradas.

```
# comentário
A B 4
A C 2
B C 1
```

### Exemplo de saída

```
$ python mst.py --input exemplos/grafo1.txt --alg kruskal
Algoritmo: Kruskal
Arestas escolhidas:
B C 1
A C 2
D E 2
C F 3
B D 5
Peso total: 13
```

Com um grafo desconexo:

```
$ python mst.py --input exemplos/grafo3_desconexo.txt --alg prim
Algoritmo: Prim
O grafo é DESCONEXO: não existe uma MST para todo o grafo.
Floresta geradora mínima (uma árvore por componente):

Componente 1 : {A, B}
A B 1
Peso: 1

Componente 2 : {C, D}
C D 2
Peso: 2

Peso total da floresta: 3
```

### Grafos de teste

| Arquivo | Resultado esperado |
|---|---|
| `exemplos/grafo1.txt` | MST com peso total 13 |
| `exemplos/grafo2_empates.txt` | MST com peso total 3 (há mais de uma MST possível) |
| `exemplos/grafo3_desconexo.txt` | Informa que o grafo é desconexo e mostra a floresta |

## Complexidade

As duas otimizações do Union-Find, compressão de caminho e união por rank, deixam cada operação em O(α(n)) amortizado, que na prática é constante (α é a inversa da função de Ackermann). Com isso, o custo do Kruskal fica dominado pela ordenação das arestas: **O(E log E)**. O Prim com heap binário roda em **O(E log V)**.

## Estrutura

```
.
├── mst.py              # Leitura do grafo, Union-Find, Kruskal, Prim e saída
├── exemplos/           # Grafos de teste
│   ├── grafo1.txt
│   ├── grafo2_empates.txt
│   └── grafo3_desconexo.txt
└── README.md
```

## Autor

**Gustavo Boeck da Silva**: Ciência de Dados e Inteligência Artificial, UFSM Campus Cachoeira do Sul
[LinkedIn](https://www.linkedin.com/in/gustavo-boeck-da-silva-1774b2233)

## Status do projeto

Concluído: atividade acadêmica entregue.
