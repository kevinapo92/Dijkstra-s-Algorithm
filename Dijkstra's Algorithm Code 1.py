import pandas as pd
"""Reference: https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/"""


class sp_graph():
	def __init__(self, graph, source, sink):
		self.V = len(graph)
		self.graph = graph
		self.source = source
		self.sink = sink
		self.sp = {i: [self.source] for i in range(self.V)}
	
	def min_distance(self, dist, sp_list):
		min = 999999
		min_index = self.source
		
		for v in range(self.V):
			if dist[v] < min and sp_list[v] == False:
				min = dist[v]
				min_index = v
		
		return min_index
	
	def print_solution(self, dist):
		print(f"Vertex and SP distance (from Source {self.source} to Sink {self.sink})")
		print(f"distance={dist[self.sink]} with path {self.sp[self.sink]}")
	
	def dijsktra(self):
		dist = [999999] * self.V
		dist[self.source] = 0
		sp_list = [False] * self.V
		
		for count in range(self.V):
			v1 = self.min_distance(dist, sp_list)
			sp_list[v1] = True
			
			for v2 in range(self.V):
				if sp_list[v2] is False and self.graph[v1][v2] > 0 and dist[v2] > dist[v1] + self.graph[v1][v2]:
					dist[v2] = dist[v1] + self.graph[v1][v2]
					self.sp[v2] = self.sp[v1] + [v2]
		
		self.print_solution(dist)


data_graph = pd.read_excel("dijkstra_input.xlsx", index_col=0)
graph_input = data_graph.values.tolist()
	
instance = sp_graph(graph=graph_input, source=0, sink=5)
instance.dijsktra()
