import unittest
import collections


def bfs_get_path(graph, start_node, end_node):

    # Find the shortest route in the network between the two users
    # BFS always finds the shourtest path but the path that DFS finds
    # is not always the shortest path
    # BFS is based on the queue and DFS is based on stack
    # In both of them do not forget to create a set for already_seen
    # nodes! 
    # So first we need a queue or deque to store the nodes that we need
    # to visit
    # Edge cases
    if (start_node not in graph) or (end_node not in graph):
        raise Exception("start_node and end_node should be in the graph!")
    nodes_to_visit = collections.deque()
    # For sure we need a set to keep the nodes already seen
    nodes_already_seen = set()
    # initialize the queue
    nodes_to_visit.append(start_node)
    # initialize the already seen nodes
    nodes_already_seen.add(start_node)
    # Ha now we need to keep the previous node that we need to pass to 
    # arrive to the current node.
    # before the start node there is no node so it initialized by None
    how_we_reached_current_node = {start_node : None}
    while nodes_to_visit:
        current_node = nodes_to_visit.popleft()
        # There is no need to update the already seen nodes here as we update 
        # the initial one out of the while loop and for the others we update it
        # in the for loop while searching the neighbors of the current_node.
        
        # Now check if the current_node is the end_node
        if current_node == end_node:
            return recunstruct_path(how_we_reached_current_node, start_node, end_node)
            
        for neighbor in graph[current_node]:
            if neighbor not in nodes_already_seen:
                nodes_already_seen.add(neighbor)
                # For sure we need to add it to queue as well otherwise
                # we will loose the connection of the nodes easily
                # Just set has add others has append Deque is basically is a list
                nodes_to_visit.append(neighbor)
                # update the how_we_reached_current_node
                how_we_reached_current_node[neighbor] = current_node

    return None
    
def recunstruct_path(how_we_reached_current_node, start_node, end_node):
    # This is the list to indicate the shortest path
    shortest_path = []
    # Traversing the how_we_reached_current_node backward
    current_node = end_node
    while current_node:
        shortest_path.append(current_node)
        # Now swap the current_node with the node previous to current one
        current_node = how_we_reached_current_node[current_node]
    # Interesting!! return shortest_path.reverse() does not work you should use it beforehand!!
    shortest_path.reverse()
    return shortest_path


















# Tests

class Test(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }

    def test_two_hop_path_1(self):
        actual = bfs_get_path(self.graph, 'a', 'e')
        expected = ['a', 'c', 'e']
        self.assertEqual(actual, expected)

    def test_two_hop_path_2(self):
        actual = bfs_get_path(self.graph, 'd', 'c')
        expected = ['d', 'a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_1(self):
        actual = bfs_get_path(self.graph, 'a', 'c')
        expected = ['a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_2(self):
        actual = bfs_get_path(self.graph, 'f', 'g')
        expected = ['f', 'g']
        self.assertEqual(actual, expected)

    def test_one_hop_path_3(self):
        actual = bfs_get_path(self.graph, 'g', 'f')
        expected = ['g', 'f']
        self.assertEqual(actual, expected)

    def test_zero_hop_path(self):
        actual = bfs_get_path(self.graph, 'a', 'a')
        expected = ['a']
        self.assertEqual(actual, expected)

    def test_no_path(self):
        actual = bfs_get_path(self.graph, 'a', 'f')
        expected = None
        self.assertEqual(actual, expected)

    def test_start_node_not_present(self):
        with self.assertRaises(Exception):
            bfs_get_path(self.graph, 'h', 'a')

    def test_end_node_not_present(self):
        with self.assertRaises(Exception):
            bfs_get_path(self.graph, 'a', 'h')


unittest.main(verbosity=2)'''
Created on Jan 16, 2019

@author: USOMZIA
'''
