'''
Created on Jun 10, 2019

@author: USOMZIA
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number 
(floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries ,
 where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
'''
# This is a graph which edges are values and vertices are a ---> b and the value is 2 but we also need to keep b --> a as 2/2
class Solution():
    def __init__(self):
        self.graph = {}
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        self.build_graph(equations, values)
        return [self.find_path(query) for query in queries]
        
        
    def build_graph(self, equations, values):
        #f:= from t:=to
        def add_edge(f, t, value):
            if f in self.graph:
                self.graph[f].append((t, value))
            else:
                self.graph[f] = [(t, value)]
            
        for vertices, value in zip(equations, values):
            # It is kind of directed graph that has both side
            f, t = vertices
            add_edge(f, t, value)
            add_edge(t, f, 1 / float(value))
            
    def find_path(self, query):
        import collections
        begin, end = query
        if begin not in self.graph or end not in self.graph:
            return -1
        
        # BFS traversal the graph
        keep_nodes = collections.deque()
        visited = set()
        keep_nodes.append((begin, 1))
        while keep_nodes:
            node, current_prod = keep_nodes.popleft()
            if node == end:
                return current_prod
            # traverse over all the neighbors
            visited.add(node)
            for neighbor, value in self.graph[begin]:
                if neighbor not in visited:
                    keep_nodes.append((neighbor, current_prod * value))
        # finished traversing if it is not found return -1
        return -1
    
equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
sol = Solution()
print sol.calcEquation(equations, values, queries)
                    
                
        
            
            
            
        
        