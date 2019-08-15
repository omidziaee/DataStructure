'''
Created on Jul 27, 2019

@author: omid
'''
# consider the input is list of connected pairs [(a,b),(a,c)] means a is connected to both a and c
class Graph():
    def __init__(self, input_list):
        self.graph = {}
        print self.build_graph(input_list)
    def build_graph(self, input_list):
        if len(input_list) == 0:
            raise ValueError("length of input array should be greatar than 0!")
        for pair in input_list:
            begin, end = pair
            if begin in self.graph:
                self.graph[begin].append(end)
            else:
                self.graph[begin] = [end]
        return self.graph
    def find_path(self, pair):
        return self.BFS(pair)
    def BFS(self, pair):
        import collections
        visited = set()
        queue = collections.deque()
        begin, end = pair
        queue.append(begin)
        path = {begin: None}
        while queue:
            node = queue.popleft()
            if node == end:
                return path
            for neigh in self.graph[begin]:
                if neigh not in visited:
                    visited.add(node)
                    path[no]
                    queue.append(neigh)
        return path
                
                
            
    
    
graph = Graph([["a","b"], ["a","c"], ["b","c"], ["c", "d"]])
print graph.find_path(["a", "d"])
    
    
    
        
    