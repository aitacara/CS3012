import unittest

class TestLCAMethod(unittest.TestCase):

    def test_3_Node_Tree(self):
        self.assertEqual(False, True)

    def test_Root_As_Result(self):
        self.assertTrue(False)
        self.assertFalse(True)

    def test_Both_Desendants_Same(self):
        self.assertTrue(False)

    def test_Both_Desendants_Same_As_Root(self):
        self.assertTrue(False)
       
if __name__ == '__main__':
    unittest.main()