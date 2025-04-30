from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    heap = [(0, 0, source)]  
    visited = {}

    while heap:
        weight, num_edges, node = heappop(heap)

        if node in visited:
            prev_weight, prev_edges = visited[node]
            if weight > prev_weight or (weight == prev_weight and num_edges >= prev_edges):
                continue

        visited[node] = (weight, num_edges)

        for v, w in graph.get(node, set()):
            if v not in visited or weight + w < visited[v][0] or (weight + w == visited[v][0] and num_edges + 1 < visited[v][1]):
                heappush(heap, (weight + w, num_edges + 1, v))

    return visited

def bfs_path(graph, source):

    parent = {}
    queue = deque()
    queue.append(source)
    parent[source] = None 

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)
    return parent

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }
    
def get_path(parents, destination):
  path = []
  current = destination

  while parents[current] is not None:
      path.append(parents[current])
      current = parents[current]

  path.reverse()
  return ''.join(path)