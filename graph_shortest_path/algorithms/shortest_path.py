import logging


class ShortestPath:
    def __init__(self, graph):
        self.graph = graph
        self.queue = list() # (weight, node, path)
        self.distances = list() # (weight, node, path)
        self.visited = set()

    def get_shortest_path(self, source):
        self.queue.append((0, source, list()))
        while self.queue:
            weight, node, path = self.queue.pop(0)
            if node in self.visited:
                continue
            logging.debug(f"Visiting node {node}")
            self.visited.add(node)
            self.distances.append((weight, node, path))
            neighbors = self.graph.loc[node][self.graph.loc[node] != 0]
            for neighbor, neighbor_weight in neighbors.items():
                if neighbor not in self.visited:
                    logging.debug(f"Adding neighbor {neighbor} of {node} with weight {weight + neighbor_weight}")
                    self.queue.append((weight + neighbor_weight, neighbor, path + [node]))
            self.queue.sort(key=lambda x: x[0])
        return self.distances