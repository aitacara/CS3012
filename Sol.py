import networkx as nx
import numpy as np
class LCA(object):

    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q):
            return root
        left, right = [self.lowestCommonAncestor(child, p, q) \
        for child in (root.left, root.right)]
        # 1. If the current subtree contains both p and q,
        #    return their LCA.
        # 2. If only one of them is in that subtree,
        #    return that one of them.
        # 3. If neither of them is in that subtree,
        #    return the node of that subtree.
        return root if left and right else left or right


    def LCA4DAG(self, graph, a, b):
        #check that the graph is of the correct type
        assert nx.is_directed_acyclic_graph(graph)
        #take out list of nodes reachable from a and b
        common_ancestors = list(nx.descendants(graph, a) & nx.descendants(graph, b))
        # get sum of path lengths
        # first create zero array representing each node reachable from a and b.
        sum_of_path_lengths = np.zeros((len(common_ancestors)))
        #traverse graph and update path lengths

        #find lowest value that is same for both leave zero if not same or put in sore if same
        return 0