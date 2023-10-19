def strongly_connected_components(G):
    R = set()
    M = 0
    N = list(G.keys())
    f = {}
    f_inv = {}
    N.sort(key=lambda v: -f.get(v, 0))
    component = {}
    K = 0

    def visit1(v):
        nonlocal M
        R.add(v)
        for w in G.get(v, []):
            if w not in R:
                visit1(w)
        M += 1
        f[v] = M
        f_inv[M] = v

    def visit2(v):
        nonlocal K
        R.add(v)
        for w, neighbors in G.items():
            if w not in R and v in neighbors:
                visit2(w)
        if K not in component.keys():
            component[K] = [v]
        else:
            component[K].append(v)

    for v in N:
        if v not in R:
            visit1(v)

    R = set()
    for i in range(len(N), 0, -1):
        v = f_inv[i]
        if v not in R:
            K += 1
            visit2(v)

    return component

def generate_example_graphs():
    graph1 = { # graph1 is identical to the graph covered in the lecture.
        'A': ['G'],
        'B': ['A'],
        'C': ['D', 'G'],
        'D': ['E'],
        'E': ['D'],
        'F': ['A', 'E'],
        'G': ['B', 'D', 'E', 'F'],
    }
    graph2 = {
        'A': ['B'],
        'B': ['C', 'D'],
        'C': ['A'],
        'D': ['E', 'F'],
        'E': ['G', 'F'],
        'F': ['G'],
        'G': ['E']
    }
    graph3 = {
        'X': ['Y'],
        'Y': ['Z', 'W'],
        'Z': ['W'],
        'W': ['V', 'U'],
        'V': ['X'],
        'U': ['V'],
        'A': ['B'],
        'B': ['C', 'D'],
        'C': ['A'],
        'D': ['E', 'F'],
        'E': ['G'],
        'F': ['G'],
        'G': []
    }
    return [graph1, graph2, graph3]


def run():
    example_graphs = generate_example_graphs()
    for i, graph in enumerate(example_graphs, start=1):
        print(f"Example {i}:")
        components = strongly_connected_components(graph)
        for component, nodes in components.items():
            print(f"Component {component}: {nodes}")
        print()

run()