import pandas as pd
import heapq as hq
"""Reference: https://gist.github.com/kachayev/5990802"""

data_graph = pd.read_excel("dijkstra_input.xlsx", index_col=0)
graph_input = data_graph.values.tolist()

def dijkstra(graph, source, sink):
	edges = {}
	for i in range(len(graph)):
		edges[i] = []
		for j in range(len(graph)):
			if graph[i][j] > 0:
				edges[i].append((graph[i][j], j))
				
	q = [(0, source, [])]
	visited = set()
	shortest = {source: 0}
	
	while True:
		(path_dist, v1, path) = hq.heappop(q)
		if v1 not in visited:
			visited.add(v1)
			path = path + [v1]
			if v1 == sink:
				return (path_dist, path)
			for (dist, v2) in edges[v1]:
				if v2 in visited:
					continue
				prev = shortest.get(v2)
				next = path_dist + dist
				if prev is None or next < prev:
					shortest[v2] = next
					hq.heappush(q, (next, v2, path))
	

print(dijkstra(graph=graph_input, source=0, sink=5))