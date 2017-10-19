import unittest
from TreeNode import Tree 
from Sol import LCA

class TestLCAMethod(unittest.TestCase):
    
    def test_3_Node_Tree(self):
        self.assertEqual(LCA.lowestCommonAncestor(dummy.root ,dummy.search(5), dummy.search(1)),dummy.search(3))

    def test_Root_As_Result(self):
        self.assertEqual(LCA.lowestCommonAncestor(dummy.root ,dummy.search(6), dummy.search(8)),dummy.search(3))

    def test_Both_Desendants_Same(self):
        self.assertEqual(LCA.lowestCommonAncestor(dummy.root ,dummy.search(8), dummy.search(8)),dummy.search(1))

    def test_Both_Desendants_Same_As_Root(self):
        self.assertEqual(LCA.lowestCommonAncestor(dummy.root ,dummy.search(3), dummy.search(3)),dummy.search(3))

    def test_Mid_Tree_Result_Right(self):
        self.assertEqual(LCA.lowestCommonAncestor(dummy.root ,dummy.search(0), dummy.search(8)),dummy.search(1))

    def test_Mid_Tree_Result_Left(self):
        self.assertEqual(LCA.lowestCommonAncestor(dummy.root ,dummy.search(2), dummy.search(6)),dummy.search(5))

    def test_Mid_Tree_Result_Left_Deeper(self):
        self.assertEqual(LCA.lowestCommonAncestor(dummy.root ,dummy.search(4), dummy.search(7)),dummy.search(2))



if __name__ == '__main__':
    dummy = Tree()
#
#         _______3______
#       /              \
#     ___5__          ___1__
#   /      \        /      \
#   6      _2       0       8
#          /  \
#          7   4
    #treevals = [3,1,5,6,2,0,8,4,7]
    dummy.add_node(3)
    dummy.add_node(1)
    dummy.add_node(5)
    dummy.add_node(6)
    dummy.add_node(2)
    dummy.add_node(0)
    dummy.add_node(8)
    dummy.add_node(4)
    dummy.add_node(7)

    print dummy.search(3).left.key
    print dummy.search(3).right.key
    unittest.main()