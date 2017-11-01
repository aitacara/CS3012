import unittest
from TreeNode import Tree 
from Sol import LCA
import matplotlib.pyplot as plt; plt.ion()
import networkx as nx

class TestLCAMethod(unittest.TestCase):
    
    def test_3_Node_Tree(self):
        self.assertEqual(caller.lowestCommonAncestor(dummy.root ,dummy.search(5), dummy.search(1)).key,dummy.search(3).key)

    def test_Root_As_Result(self):
        self.assertEqual(caller.lowestCommonAncestor(dummy.root ,dummy.search(1), dummy.search(6)).key,dummy.search(3).key)

    def test_Both_Desendants_Same(self):
        self.assertEqual(caller.lowestCommonAncestor(dummy.root ,dummy.search(8), dummy.search(8)).key,dummy.search(8).key)

    def test_Both_Desendants_Same_As_Root(self):
        self.assertEqual(caller.lowestCommonAncestor(dummy.root ,dummy.search(3), dummy.search(3)).key,dummy.search(3).key)

    def test_Mid_Tree_Result_Right(self):
        self.assertEqual(caller.lowestCommonAncestor(dummy.root ,dummy.search(4), dummy.search(6)).key,dummy.search(5).key)

    def test_Mid_Tree_Result_Left(self):
        self.assertEqual(caller.lowestCommonAncestor(dummy.root ,dummy.search(2), dummy.search(0)).key,dummy.search(1).key)

    def test_Mid_Tree_Result_Left_Deeper(self):
        self.assertEqual(caller.lowestCommonAncestor(dummy.root ,dummy.search(7), dummy.search(8)).key,dummy.search(8).key)

    def test_Mid_Tree_Result_Left_split_level(self):
        self.assertEqual(caller.lowestCommonAncestor(dummy.root ,dummy.search(7), dummy.search(4)).key,dummy.search(5).key)

    #Tests for DAG LCA
    def test_Two_In_Line(self):
        self.assertEqual(caller.LCA4DAG(G, 'c', 'b'), ['a'])

    def test_In_seprate_branch(self):
        self.assertEqual(caller.LCA4DAG(G, 'e', 'c'), ['b'])

    def test_In_seprate_branch_1(self):
        self.assertEqual(caller.LCA4DAG(G, 'd', 'f'), ['b'])

    def test_In_same_branch(self):
        self.assertEqual(caller.LCA4DAG(G, 'b', 'd'), ['a'])

    def test_same_node(self):
        self.assertEqual(caller.LCA4DAG(G, 'c', 'c'), ['b'])

    def test_use_root_node(self):
        self.assertEqual(caller.LCA4DAG(G, 'g', 'f'), ['e'])  

    def test_use_terminal_node(self):
        self.assertEqual(caller.LCA4DAG(G, 'a', 'b'), ['none'])   







if __name__ == '__main__':
    caller =LCA()
    dummy = Tree()
    dummy.add_node(3)
    dummy.add_node(1)
    dummy.add_node(5)
    dummy.add_node(6)
    dummy.add_node(2)
    dummy.add_node(0)
    dummy.add_node(8)
    dummy.add_node(4)
    dummy.add_node(7)
    dummy.traverse()

    nodes = ["a","b","c","d","e","f","g"]
    edges = [("g","d"),
             ("g","f"),
             ("d","c"),
             ("c","b"),
             ("b","a"),
             ("f","e"),
             ("e","b"),]

    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    # plot
    pos = nx.spring_layout(G)
    nx.draw(G, pos)
    nx.draw_networkx_labels(G, pos, labels=dict([(c, c) for c in 'abcdefg']))
    plt.show(block=True)
    print "Close graph to continue"
    unittest.main()