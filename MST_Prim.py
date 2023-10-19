# Global variable
total_cost = 0

# Defining a binary heap class for the purpose of using a priority queue.
# The class also includes the implementation of counting each heap operation.
class BinaryMinHeap:
    def __init__(self):
        self.items = []
        self.num_decrease_key = 0
        self.num_insert = 0
        self.num_delete_min = 0

    def left_child_index(self, i):
        return 2 * i + 1

    def right_child_index(self, i):
        return 2 * i + 2

    def parent_index(self, i):
        return (i - 1) // 2

    def insert_node(self, node, cost):
        entry = (node, cost)
        self.items.append(entry)
        self.heapify_up(len(self.items) - 1)
        self.num_insert += 1  # count insertion operation.

    def extract_min(self):
        if len(self.items) == 0:
            return None
        if len(self.items) == 1:
            self.num_delete_min += 1  # count delete min operation.
            return self.items.pop()

        root = self.items[0]
        self.items[0] = self.items.pop()
        self.heapify_down(0)
        self.num_delete_min += 1  # count delete min operation.
        return root

    def decrease_key(self, target, new_cost):
        for i, (node, cost) in enumerate(self.items):
            if node == target:
                self.items[i] = (target, new_cost)
                self.heapify_up(i)
        self.num_decrease_key += 1  # count decrease key operation.

    def heapify_up(self, i):
        while i > 0 and self.items[i][1] < self.items[self.parent_index(i)][1]:
            self.items[i], self.items[self.parent_index(i)] = self.items[self.parent_index(i)], self.items[i]
            i = self.parent_index(i)

    def heapify_down(self, i):
        left = self.left_child_index(i)
        right = self.right_child_index(i)
        smallest = i

        if left < len(self.items) and self.items[left][1] < self.items[i][1]:
            smallest = left
        if right < len(self.items) and self.items[right][1] < self.items[smallest][1]:
            smallest = right

        if i != smallest:
            self.items[i], self.items[smallest] = self.items[smallest], self.items[i]
            self.heapify_down(smallest)

    def print_how_many_heap_operation(self):
        print("########################################################")
        print("### How many times each heap operation is performed?")
        print("* Number of decrease Key operation :", self.num_decrease_key)  # at most m times.
        print("* Number of insertion operation :", self.num_insert)  # n-1 times only once for each node.
        print("* Number of delete-min operation :", self.num_delete_min)  # n-1 times
        print("########################################################")


def prim_algorithm(graph, initial_node):
    global total_cost
    minheap = BinaryMinHeap()
    big_N = 10000000  # define "big_N" in place of infinity for usage.
    V_G = list(graph.keys())  # V(G)
    v = initial_node  # choose initial node v
    l = {}
    mst = []
    V_T = [v]  # V(T)

    # Set l_w to large number.
    for i in V_G:
        if i != v:
            l[i] = (-1, big_N)

    while len(V_T) < len(V_G):
        for (w, c) in graph[v]:
            if w not in V_T:
                if c < l[w][1] < big_N:  # at most m times
                    l[w] = (v, c)        # l_w <- c(e)
                    minheap.decrease_key(w, c)
                elif l[w][1] == big_N:   # n-1 times only once for each node
                    l[w] = (v, c)        # l_w <- c(e)
                    minheap.insert_node(w, c)

        (v, l_v) = minheap.extract_min()
        total_cost += l_v
        mst.append((l[v][0], v, l_v))
        V_T.append(v)
    # print results
    minheap.print_how_many_heap_operation()

    return mst


def run(graph, initial_node):
    init_node = initial_node
    minimum_spanning_tree = prim_algorithm(graph, init_node)
    formatted_mst = [(v, w, c) for (v, w, c) in minimum_spanning_tree]
    print("* Minimum Spanning Tree:", formatted_mst)
    print("* Total Cost:", total_cost)
    print("")


# Run the code by including the initial node within the "run" function.
# Depending on the initial node, the number of "decrease key" operations may vary,
# resulting in different output counts.
graph_1 = {
    1: [(2, 3), (4, 7), (5, 8)],
    2: [(1, 3), (3, 1), (4, 4)],
    3: [(2, 1), (4, 2)],
    4: [(1, 7), (2, 4), (3, 2), (5, 3)],
    5: [(1, 8), (4, 3)]
}
# from mst lecture
graph_2 = {
    1: [(2, 2), (3, 3)],
    2: [(1, 2), (3, 1), (4, 4), (5, 5)],
    3: [(1, 3), (2, 1), (5, 2)],
    4: [(2, 4), (5, 1), (6, 3)],
    5: [(2, 5), (3, 2), (4, 1), (6, 2)],
    6: [(4, 3), (5, 2)]
}

run(graph_1, 1)
run(graph_2, 1)