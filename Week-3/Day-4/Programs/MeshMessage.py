import unittest


from collections import deque


def path_reconstruction(previouslist, start_node, end_node):
    shortpath_reverse = []
    current_node = end_node
    while current_node:
        shortpath_reverse.append(current_node)
        current_node = previouslist[current_node]
    shortpath_reverse.reverse()  
    return shortpath_reverse  


def bfs_get_path(graph, start_node, end_node):
    if start_node not in graph:
        raise Exception
    if end_node not in graph:
        raise Exception

    tovisitnodes = deque()
    tovisitnodes.append(start_node)
    tracker = {start_node: None}

    while len(tovisitnodes) > 0:
        current = tovisitnodes.popleft()
        if current == end_node:
            return path_reconstruction(tracker, start_node, end_node)

        for side in graph[current]:
            if side not in tracker:
                tovisitnodes.append(side)
                tracker[side] = current
    return None


















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


unittest.main(verbosity=2)